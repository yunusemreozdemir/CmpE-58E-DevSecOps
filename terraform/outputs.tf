output "cluster_name" {
  value = google_container_cluster.primary.name
}

output "repo_url" {
  value = google_artifact_registry_repository.fastapi_repo.repository_id
}
