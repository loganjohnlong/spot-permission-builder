import click

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
        raise click.BadParameter(f'Invalid cloud provider. valid options are: {cloud_providers}')
    return value

def validate_products(ctx, param, value):
    if not value:
        raise click.BadParameter("At least one product must be selected.")
    for product in value:
        if product not in product_options:
            raise click.BadParameter(f'Invalid product: {product}. valid options are {product_options}')
    return value

################
# MAIN FUNCTION
################
@click.command()
@click.option('--cloud', '-c', type=click.Choice(cloud_providers, case_sensitive=False), callback=validate_cloud, help='Cloud provider to build permissions for')
@click.option('--products', '-p', type=click.Choice(product_options, case_sensitive=False), multiple=True, callback=validate_products, help='Spot products that the customer wishes to use. Use this flag multiple times if specifying multiple products.')
def main(cloud, products):
    """Builds permissions for a given cloud provider and product(s)"""
    if cloud == 'AWS':
        print("Performing AWS-specific tasks")
    elif cloud == 'Azure':
        print("Performing Azure-specific tasks")
    elif cloud == 'GCP':
        print("Performing GCP-specific tasks")

if __name__ == '__main__':
    main()
