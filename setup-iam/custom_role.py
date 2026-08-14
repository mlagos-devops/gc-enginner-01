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