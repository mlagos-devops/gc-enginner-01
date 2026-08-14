# Proyecto Practicas Google Cloud Engineer

### Para el proyecto se utilizara como Stack Tecnologico:
#### IaC: Terraform
#### Scripting: Bash & Python 3
#### CLI: Gcloud sdk & kubecti
#### GCP Services: Compute Engine, GKE, Cloud Run, Cloud SQL, BigQuery, VPC

### Se ira construyendo Módulo a Módulo
#### Módulo 1: Configuraremos un entorno seguro (IAM, VPCs personalizadas y Firewalls) usando Código.
#### Módulo 2: Crearemos Grupos de Instancias Administrados (MIGs) con auto-escalado.
#### Módulo 3: Desplegaremos contenedores en Kubernetes (GKE) y servicios Serverless (Cloud Run & Functions).
#### Módulo 4: Conectaremos bases de datos (Cloud SQL, BigQuery) y almacenamiento (GCS).
#### Módulo 5: Configuraremos alertas de caída de servicio y exportación de logs.

# Módulo 1: Configuraremos un entorno seguro (IAM, VPCs personalizadas y Firewalls) usando Código.
## Google Cloud Engineer - v01
### 1 - Automatizando el Setup con Terraform (APIs)

#### main.tf
```
provider "google" {
  project = "gc-enginner-01"
  region  = "us-central1"
}

resource "google_project_service" "apis" {
  for_each = toset(["compute.googleapis.com", "container.googleapis.com", "cloudresourcemanager.googleapis.com"])
  service  = each.key
  disable_on_destroy = false
}
```

### 2 - Service Accounts y IAM con Bash
#### Comandos Usados
Lanzar el Script de roles en python
python3 custom_role.py
Verificar libreria requerida: "pip install google-cloud-iam"

#### setup_iam.sh
```
gcloud iam service-accounts create dev-deployer --display-name "Deployer ML"

gcloud projects add-iam-policy-binding gc-enginner-01 --member="serviceAccount:dev-deployer@gc-enginner-01.iam.gserviceaccount.com" --role="roles/compute.viewer"
```

### 3 - Creando Roles Personalizados con Python
#### custon_role.py
```
import argparse
from google.cloud import iam_admin_v1

def create_role(project_id, role_id):
    client = iam_admin_v1.IAMClient()
    parent = f"projects/{project_id}"
    role = iam_admin_v1.Role(
        title="VM Iniciar Detener",
        included_permissions=["compute.instances.start", "compute.instances.stop"],
        stage=iam_admin_v1.Role.RoleLaunchStage.GA
    )
    request = iam_admin_v1.CreateRoleRequest(parent=parent, role_id=role_id, role=role)
    response = client.create_role(request=request)
    print(f"Rol creado: {response.name}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a custom IAM role.")
    parser.add_argument("project_id", help="The Google Cloud Project ID")
    parser.add_argument("role_id", help="The ID of the custom role to create")

    args = parser.parse_args()

    create_role(args.project_id, args.role_id)
```


### 4 - Desplegando una VPC Segura (No default)
.
..
...

### 5 - Firewalls y Network Tags
.
..
...
