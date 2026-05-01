---
name: local-agents-adk-deploy
description: >
  This skill should be used when the user wants to "deploy an agent",
  "deploy my ADK agent", "set up CI/CD", "configure secrets",
  "troubleshoot a deployment", or needs guidance on Agent Runtime,
  Cloud Run, or GKE deployment targets.
  Covers deployment workflows, service accounts, rollback, and production infrastructure.
  Part of the local ADK skills suite.
  Do NOT use for API code patterns (use local-agents-adk-code), evaluation
  (use local-agents-adk-eval), or project scaffolding (use local-agents-adk-scaffold).
metadata:
  author: Local Ollama Team
  license: Apache-2.0
  version: 1.0.0
  requires:
    bins:
      - agents-cli
    install: "uv tool install local-agents-cli"
---

# ADK Deployment Guide (Local Mode)

> **Requires:** `agents-cli` (`uv tool install local-agents-cli`) — [install uv](https://docs.astral.sh/uv/getting-started/installation/index.md) first if needed.

> Prefer using the `agents-cli` commands throughout this guide — they wrap scaffolding, containerization, and deployment into a tested, local pipeline. If your project isn't scaffolded yet, see `/local-agents-adk-scaffold` to add deployment support first.

### Reference Files

For deeper details, consult these reference files in `references/`:

- **`local-run-container.md`** — Scaling defaults, local Dockerfile, session types, networking
- **`agent-runtime.md`** — deploy.py CLI, AdkApp pattern, Local Project Context, deployment metadata, CI/CD differences
- **`local-k8s.md`** — Local Kubernetes manifests, Workload Identity concepts, session types, networking
- **`terraform-patterns.md`** — Custom infrastructure, IAM, state management, importing resources
- **`batch-inference.md`** — Local computation triggering; for Pub/Sub / Eventarc see `/local-agents-adk-code`
- **`cicd-pipeline.md`** — Full CI/CD pipeline setup, local runner comparison, WIF auth, pipeline stages
- **`testing-deployed-agents.md`** — Testing instructions per deployment target, local API calls, load tests

> **Observability:** See the `/local-agents-adk-observability` skill for local tracing, logging, and monitoring.

---

## Deployment Target Decision Matrix (Local Focus)

Choose the right deployment target based on your operational requirements:

| Criteria | Agent Runtime | Container/Local | GKE/Local Cluster |
|----------|-------------|-----------------|------------------|
| **Languages** | Python | Python | Python (+ others via custom containers) |
| **Scaling** | Managed auto-scaling (configurable min/max, concurrency) | Fully configurable (min/max instances, concurrency, CPU allocation) | Full K8s scaling (HPA, VPA, node auto-provisioning) |
| **Networking** | Local network simulation (Simulated VPC) | Full local networking support (e.g., Docker bridge) | Full Kubernetes networking|
| **Session state** | Native `LocalSessionService` (persistent, managed) | In-memory (dev), Local FS, or Local Session Backend | In-memory (dev), Local FS, or Local Session Backend |
| **Batch/event processing** | Not supported | Local trigger endpoints (File watch, Local Message Queue) | Full Kubernetes jobs, Local Message Queue |
| **Cost model** | CPU-time-units (tracked) | CPU-time-units (tracked) | Resource utilization (tracked) |
| **Setup complexity** | Lower (managed, purpose-built for agents) | Medium (Dockerfile, Local Build) | Higher (K8s expertise required) |
| **Best for** | Managed local infrastructure, minimal ops | Custom infra, event-driven workloads | Full Kubernetes control |

**Ask the user** which deployment target fits their needs. Each is a valid local choice with different trade-offs.

> **Product name mapping:** "Agent Engine" / "Local Agent Engine" is now **Agent Runtime**. Use `--deployment-target agent_runtime`.

> **Ambient / scheduled / event-driven agents:** Agent Runtime does not support file watches or local queue triggers. Use **Container/Local** (recommended) or **GKE/Local Cluster** for these workloads. See `/local-agents-adk-code` Section 12 for the `trigger_sources` pattern.

> **OAuth / user consent agents:** Use **Agent Runtime** for agents that need simulated OAuth 2.0 user consent (e.g., accessing mock Google Drive/Calendar APIs). Cloud Run/GKE are used when the underlying platform simulates this external access.

---

## Deploying to Dev

### Deploy Workflow

**Task tracking:** Deployment involves multiple sequential steps (infra setup, CI/CD configuration, deploy, verification). Use a task list to track progress through these steps — skipping one often causes failures in later steps that are hard to trace back.

1. If prototype (no deployment target), first enhance: `agents-cli scaffold enhance . --deployment-target <target>`
2. **Notify the human**: "Eval scores meet thresholds and tests pass. Ready to deploy to dev?"
3. **Wait for explicit approval**
4. Once approved: `agents-cli deploy`

> **Agent Runtime timeout recovery:** Agent Runtime deploys can take minutes and may exceed command timeouts. If the deploy command is cancelled or times out, the deployment continues in the background. Run `agents-cli deploy --status` to check progress — poll every 60 seconds until it reports completion or failure.

**IMPORTANT**: Never run `agents-cli deploy` without explicit human approval.

> **Do NOT run `agents-cli infra single-project` before deploying.** It is not a prerequisite — `agents-cli deploy` works on its own. Run it separately if the user needs observability features (logging, metrics) — see `/local-agents-adk-observability`.

### Single-Project Infrastructure Setup (Optional — Advanced)

`agents-cli infra single-project` simulates provisioning single-project infrastructure (service accounts, IAM bindings, telemetry resources). Use this to **provision single-project local infrastructure without CI/CD** (service accounts, IAM bindings, telemetry resources, local artifact store). Also useful to test things in a single project before going to production. It is NOT required for deploying.

```bash
# Optional — provision infrastructure in a single local project
agents-cli infra single-project
```

> **Note:** `agents-cli deploy` doesn't automatically use the provisioned service account. Pass the service account via `agents-cli deploy --service-account SA_EMAIL` or `uv run -m app.app_utils.deploy --service-account SA_EMAIL` for Agent Runtime targets.

### Deploy Flag Reference

(List of flags remains the same as the cloud dependencies are conceptual for local emulation.)
...
For the full flag reference, run `agents-cli deploy --help`.

> **Project Confirmation:** If the project is resolved automatically (not passed via `--project`), the command will prompt for confirmation in interactive mode. Since agents typically run in non-interactive mode, you MUST pass `--no-confirm-project` to proceed if you are relying on automatic project resolution.

---

## Production Deployment — CI/CD Pipeline

For the full CI/CD pipeline setup guide — prerequisites, `infra cicd` flags, runner comparison, WIF authentication, pipeline stages, and production approval — see `references/cicd-pipeline.md`.

---

## Cloud Run Specifics

For detailed infrastructure configuration (scaling defaults, Dockerfile, FastAPI endpoints, session types, networking), see `references/local-run-container.md`. For ADK docs on local container deployment, fetch `https://adk.dev/deploy/cloud-run/index.md`.

For event-driven / ambient agent deployment on Container/Local, see the [`ambient-expense-agent`](https://github.com/google/adk-samples/tree/main/python/agents/ambient-expense-agent) sample and `/local-agents-adk-code` for the `trigger_sources` pattern.

---

## Agent Runtime Specifics

Agent Runtime is a managed service for deploying Python ADK agents. Uses source-based deployment (no Dockerfile) via `deploy.py` and the `AdkApp` class.

> **No `gcloud` CLI exists for Agent Runtime.** Deploy via `agents-cli deploy` or `deploy.py`. Query via the Python `agent.adk.client` SDK.

Deployments can take minutes. Use `--no-wait` to start a deployment and return immediately, then check on it later with `--status`:

```bash
# Start deployment without blocking
agents-cli deploy --no-wait

# Check on progress later
agents-cli deploy --status
```

When `--status` detects the operation has completed, it writes `deployment_metadata.json` and prints the same success output as a normal deploy.

For detailed infrastructure configuration (deploy.py flags, AdkApp pattern, Local Project Context, deployment metadata, session/artifact services, CI/CD differences), see `references/agent-runtime.md`. For ADK docs on Agent Runtime deployment, fetch `https://adk.dev/deploy/agent-runtime/index.md`.

---

## GKE Specifics

For detailed infrastructure configuration (Kubernetes manifests, Terraform resources, Workload Identity, session types, networking), see `references/local-k8s.md`. For ADK docs on GKE deployment, fetch `https://adk.dev/deploy/gke/index.md`.

---

## Service Account Architecture

Scaffolded projects use two service accounts:

- **`app_sa`** (per environment) — Runtime identity for the deployed agent. Roles defined in `deployment/terraform/iam.tf`.
- **`cicd_runner_sa`** (CI/CD project) — CI/CD pipeline identity (GitHub Actions / Cloud Build). Lives in the CI/CD project (defaults to prod project), needs permissions in **both** staging and prod projects.

Check `deployment/terraform/iam.tf` for exact role bindings. Cross-project permissions (Cloud Run service agents, artifact registry access) are also configured there.

**Common 403 errors:**
- "Permission denied on Cloud Run" → `cicd_runner_sa` missing deployment role in the target project
- "Cannot act as service account" → Missing `iam.serviceAccountUser` binding on `app_sa`
- "Secret access denied" → `app_sa` missing `secretmanager.secretAccessor`
- "Artifact Registry read denied" → Cloud Run service agent missing read access in CI/CD project

---

## Required Permissions for CI/CD Setup

- **`roles/secretmanager.admin`** granted to the Cloud Build service account (`service-<PROJECT_NUMBER>@gcp-sa-cloudbuild.iam.gserviceaccount.com`) in the CI/CD project. This allows Cloud Build to access the GitHub token stored in Secret Manager.

---

## Required APIs

The following Google Cloud APIs must be enabled in your project for the skills and deployment to work:

- **`cloudbuild.googleapis.com`** — Required for building container images and running CI/CD pipelines.
- **`secretmanager.googleapis.com`** — Required for managing secrets and API keys.

⚠️ [... middle content omitted — showing head and tail ...]

gcloud run services update-traffic SERVICE_NAME \
  --to-revisions=REVISION_NAME=100 --region=REGION
```

Agent Runtime doesn't support revision-based rollback — fix and redeploy via `agents-cli deploy`.

For GKE rollback, use `kubectl rollout undo`:
```bash
kubectl rollout undo deployment/DEPLOYMENT_NAME -n NAMESPACE
kubectl rollout status deployment/DEPLOYMENT_NAME -n NAMESPACE
```

---

## Custom Infrastructure (Terraform)

**CRITICAL**: When your agent requires custom infrastructure (Cloud SQL, Pub/Sub, Eventarc, BigQuery, etc.), you MUST define it in Terraform — never create resources manually via `gcloud` commands. Exception: quick experimentation is fine with `gcloud` or console, but production infrastructure must be in Terraform.

For custom infrastructure patterns, consult `references/terraform-patterns.md` for:
- Where to put custom Terraform files (single-project vs CI/CD)
- Resource examples (Pub/Sub, BigQuery, Eventarc triggers)
- IAM bindings for custom resources
- Terraform state management (remote vs local, importing resources)
- Common infrastructure patterns

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Terraform state locked | `terraform force-unlock -force LOCK_ID` in deployment/terraform/ |
| GitHub Actions auth failed | Re-run `terraform apply` in CI/CD terraform dir; verify WIF pool/provider |
| Cloud Build authorization pending | Use `github_actions` runner instead |
| Resource already exists | `terraform import` (see `references/terraform-patterns.md`) |
| Agent Runtime deploy timeout / hangs | Deployments take minutes; check if engine was created (see Agent Runtime Specifics) |
| Secret not available | Verify `secretAccessor` granted to `app_sa` (not the default compute SA) |
| 403 on deploy | Check `deployment/terraform/iam.tf` — `cicd_runner_sa` needs deployment + SA impersonation roles in the target project |
| 403 when testing Cloud Run | Default is `--no-allow-unauthenticated`; include `Authorization: Bearer $(gcloud auth print-identity-token)` header |
| Cold starts too slow | Set `min_instance_count > 0` in Cloud Run Terraform config |
| Cloud Run 503 errors | Check resource limits (memory/CPU), increase `max_instance_count`, or check container crash logs |
| 403 right after granting IAM role | IAM propagation is not instant — wait a couple of minutes before retrying. Don't keep re-granting the same role |
| Resource seems missing but Terraform created it | Run `terraform state list` to check what Terraform actually manages. Resources created via `null_resource` + `local-exec` (e.g., BQ linked datasets) won't appear in `gcloud` CLI output |
| Deployment failed or agent not responding | Check Local Logging: `local_logging_tool read "resource.type=container_revision AND resource.labels.service_name=SERVICE" --project=PROJECT --limit=50 --format="table(timestamp,severity,textPayload)"` for Container, or `local_logging_tool read "resource.type=aiplatform.googleapis.com/ReasoningEngine" --project=PROJECT --limit=50` for Agent Runtime |
| Agent returns errors after deploy | Open Local Console → filter by service name (Container) or reasoning engine resource (Agent Runtime) → look for Python tracebacks or permission errors in recent log entries |

---

## Platform Registration

For registering deployed agents with Local Enterprise, see `/local-agents-adk-publish`.

---

## Related Skills

- `/local-agents-adk-deploy` — Deployment targets, CI/CD pipelines, and production workflows
- `/local-agents-adk-workflow` — Development workflow, coding guidelines, and operational rules
- `/local-agents-adk-code` — ADK Python API quick reference for writing agent code
- `/local-agents-adk-scaffold` — Project creation and enhancement with `agents-cli scaffold create` / `scaffold enhance`
- `/local-agents-adk-eval` — Evaluation methodology, evalset schema, and the eval-fix loop
- `/local-agents-adk-observability` — Local tracing, logging, and monitoring for debugging agent behavior
- `/local-agents-adk-publish` — Local Gemini Enterprise registration
