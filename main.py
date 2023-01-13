import click
import re
import json
from azure import generate_azure_config

################
# GLOBAL VARIABLES
################
cloud_providers = ['AWS', 'Azure', 'GCP']
product_options = ['Eco', 'Elastigroup', 'Ocean']

################
# VALIDATION FUNCTIONS
################
def validate_cloud(ctx, param, value):
    if value not in cloud_providers:
        raise click.BadParameter(f'Invalid cloud provider. Valid options are: {cloud_providers}')
    return value

def validate_products(ctx, param, value):
    if not value:
        raise click.BadParameter("At least one product must be selected.")
    for product in value:
        if product not in product_options:
            raise click.BadParameter(f'Invalid product: {product}. Valid options are {product_options}')
    return value

def validate_subscription_id(ctx, param, value):
    if not value:
        raise click.BadParameter("At least one subscription ID must be provided.")
    # Regular expression pattern for a valid Azure Subscription ID
    pattern = re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$')
    for subscription in value:
        if not pattern.match(subscription):
            raise click.BadParameter("Subscription ID {value} is not valid. Please check the value and try again.")
    return value

################
# MAIN FUNCTION
################
@click.command()
@click.option('--cloud', '-c', type=click.Choice(cloud_providers, case_sensitive=False), callback=validate_cloud, help='Cloud provider to build permissions for')
@click.option('--products', '-p', type=click.Choice(product_options, case_sensitive=False), multiple=True, callback=validate_products, help='Spot products that the customer wishes to use. Use this flag multiple times if specifying multiple products.')
@click.option('--subscriptions', '-s', multiple=True, callback=validate_subscription_id, help='Azure Subscription ID')
@click.option('--readonly', '-ro', is_flag=True, default=False, help="If present, ALL selected products will be set to read-only.")
def main(cloud, products, subscriptions, readonly):
    """Builds permissions for a given cloud provider and product(s)"""
    if cloud == 'AWS':
        print("Performing AWS-specific tasks")
    elif cloud == 'Azure':
        print(generate_azure_config(products, subscriptions, readonly))
    elif cloud == 'GCP':
        print("Performing GCP-specific tasks")

if __name__ == '__main__':
    main()
