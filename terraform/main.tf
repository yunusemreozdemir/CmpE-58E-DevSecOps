provider "google" {
  project = var.project_id
  region  = var.region
}

resource "google_artifact_registry_repository" "fastapi_repo" {
  location      = var.region
  repository_id = var.repo_name
  description   = "Artifact Registry for FastAPI App"
  format        = "DOCKER"
}

resource "google_container_cluster" "primary" {
  name     = "fastapi-cluster"
  location = var.region

  remove_default_node_pool = true
  initial_node_count       = 1

  node_config {
    machine_type = "e2-medium"
    disk_size_gb = 20
    oauth_scopes = [
      "https://www.googleapis.com/auth/cloud-platform"
    ]
  }
}

resource "google_container_node_pool" "primary_nodes" {
  name       = "default-node-pool"
  cluster    = google_container_cluster.primary.name
  location   = var.region
  node_count = 1

  node_config {
    preemptible  = false
    machine_type = "e2-medium"
    disk_size_gb = 20
    oauth_scopes = [
      "https://www.googleapis.com/auth/cloud-platform"
    ]
  }
}
