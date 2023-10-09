import boto3
from kubernetes import client, config
from kubernetes.client.rest import ApiException

def get_eks_cluster_info(cluster_name, region):
    try:
        # Initialize a Boto3 EKS client for the specified region
        eks_client = boto3.client('eks', region_name=region)

        # Describe the specified EKS cluster
        cluster_info = eks_client.describe_cluster(name=cluster_name)

        return cluster_info

    except Exception as e:
        return str(e)

def get_k8s_cluster_info(cluster_info):
    try:
        # Load Kubernetes configuration
        config.load_kube_config()

        # Initialize a Kubernetes API client
        kube_api = client.CoreV1Api()

        # Get the number of nodes in the EKS cluster
        nodes = kube_api.list_node()
        num_nodes = len(nodes.items)

        # Get the number of pods/workloads in the cluster
        workloads = kube_api.list_pod_for_all_namespaces()
        num_workloads = len(workloads.items)

        return num_nodes, num_workloads

    except ApiException as e:
        return str(e)

if __name__ == "__main__":
    # Specify the name of the EKS cluster and the AWS region
    cluster_name = "your-cluster-name"
    region = "your-region"

    cluster_info = get_eks_cluster_info(cluster_name, region)

    if isinstance(cluster_info, dict):
        eks_cluster_name = cluster_info['cluster']['name']
        eks_cluster_status = cluster_info['cluster']['status']
        eks_k8s_version = cluster_info['cluster']['version']
        eks_provider = cluster_info['cluster']['platform']
        eks_api_server_endpoint = cluster_info['cluster']['endpoint']
        eks_platform_version = cluster_info['cluster']['platformVersion']
        eks_logging_types = cluster_info['cluster']['logging']
        eks_vpc_id = cluster_info['cluster']['resourcesVpcConfig']['vpcId']

        # Check if all logging types are enabled
        all_logging_enabled = all(log['enabled'] for log in eks_logging_types)

        num_nodes, num_workloads = get_k8s_cluster_info(cluster_info)

        print(f"Cluster Name: {eks_cluster_name}")
        print(f"Status: {eks_cluster_status}")
        print(f"Kubernetes Version: {eks_k8s_version}")
        print(f"Provider: {eks_provider}")
        print(f"API Server Endpoint: {eks_api_server_endpoint}")
        print(f"Platform Version: {eks_platform_version}")
        print(f"Number of Nodes: {num_nodes}")
        print(f"VPC ID: {eks_vpc_id}")
        print(f"Logging Enabled (All Types): {all_logging_enabled}")
        print(f"Number of Workloads/Pods: {num_workloads}")
    else:
        print(f"Failed to retrieve cluster information: {cluster_info}")
