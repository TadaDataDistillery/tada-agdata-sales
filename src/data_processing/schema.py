from typing import Dict

from data_processing import parser
from data_processing import validator as va

sales_report_schema: Dict[str, va.DataFrameSchema] = {
    "raw": va.DataFrameSchema(
        {
            "grower_site_id": va.Column(int),
            "grower_house_id": va.Column(float, nullable=True),
            "grower_site_name": va.Column(str, nullable=True),
            "grower_first_name": va.Column(str, nullable=True),
            "grower_last_name": va.Column(str, nullable=True),
            "grower_address": va.Column(str, nullable=True),
            "grower_city_name": va.Column(str, nullable=True),
            "grower_province_name": va.Column(str, nullable=True),
            "grower_postal": va.Column(str, nullable=True),
            "grower_phone": va.Column(
                str, nullable=True, parsers=[parser.parse_phone_numbers]
            ),
            "grower_email": va.Column(str, nullable=True),
            "grower_cellular": va.Column(
                str, nullable=True, parsers=[parser.parse_phone_numbers]
            ),
            "grower_contact_phone": va.Column(
                str, nullable=True, parsers=[parser.parse_phone_numbers]
            ),
            "territory_rep": va.Column(str, nullable=True),
            "soil_zone": va.Column(str, nullable=True),
        }
    )
}

growers_extract_schema: Dict[str, va.DataFrameSchema] = {
    "site": va.DataFrameSchema(
        {
            "site_id": va.Column(int),
            "house_id": va.Column(float, nullable=True),
            "site_type_id": va.Column(str, nullable=True),
            "site_type": va.Column(str, nullable=True),
            "site_name": va.Column(str, nullable=True),
            "status_id": va.Column(float, nullable=True),
            "status": va.Column(str, nullable=True),
            "pay_to_name": va.Column(str, nullable=True),
            "phone": va.Column(
                str, nullable=True, parsers=[parser.parse_phone_numbers]
            ),
            "fax": va.Column(str, nullable=True, parsers=[parser.parse_phone_numbers]),
            "email": va.Column(str, nullable=True),
            "cellular": va.Column(
                str, nullable=True, parsers=[parser.parse_phone_numbers]
            ),
        }
    ),
    "address": va.DataFrameSchema(
        {
            "address_id": va.Column(int),
            "site_id": va.Column(float, nullable=True),
            "address_type_id": va.Column(str, nullable=True),
            "address_type": va.Column(str, nullable=True),
            "address": va.Column(str, nullable=True),
            "city_name": va.Column(str, nullable=True),
            "province_name": va.Column(str, nullable=True),
            "postal": va.Column(str, nullable=True),
            "soil_zone": va.Column(str, nullable=True),
            "left_over": va.Column(str, nullable=True),
            "box": va.Column(str, nullable=True),
            "rr": va.Column(str, nullable=True),
            "gd": va.Column(str, nullable=True),
            "hwy": va.Column(str, nullable=True),
            "lot": va.Column(str, nullable=True),
            "site": va.Column(str, nullable=True),
            "comp": va.Column(str, nullable=True),
            "rang": va.Column(str, nullable=True),
            "conc": va.Column(str, nullable=True),
            "grp": va.Column(str, nullable=True),
            "direction": va.Column(str, nullable=True),
        },
    ),
    "contact": va.DataFrameSchema(
        {
            "contact_id": va.Column(int),
            "site_id": va.Column(float, nullable=True),
            "primary_contact": va.Column(
                bool, nullable=True, parsers=[parser.parse_boolean]
            ),
            "contact_prefix_id": va.Column(float, nullable=True),
            "contact_prefix": va.Column(str, nullable=True),
            "first_name": va.Column(str, nullable=True),
            "middle_name": va.Column(str, nullable=True),
            "last_name": va.Column(str, nullable=True),
            "title": va.Column(str, nullable=True),
            "position_id": va.Column(float, nullable=True),
            "position": va.Column(str, nullable=True),
            "status_id": va.Column(float, nullable=True),
            "status": va.Column(str, nullable=True),
            "home_phone": va.Column(
                str, nullable=True, parsers=[parser.parse_phone_numbers]
            ),
            "phone": va.Column(
                str, nullable=True, parsers=[parser.parse_phone_numbers]
            ),
            "cellular": va.Column(
                str, nullable=True, parsers=[parser.parse_phone_numbers]
            ),
            "fax": va.Column(str, nullable=True, parsers=[parser.parse_phone_numbers]),
            "email": va.Column(str, nullable=True),
            "post_name": va.Column(str, nullable=True),
            "language_id": va.Column(float, nullable=True),
            "language": va.Column(str, nullable=True),
        }
    ),
    "preferred_contact_method": va.DataFrameSchema(
        {
            "site_id": va.Column(int),
            "contact_method_id": va.Column(float, nullable=True),
            "contact_method": va.Column(str, nullable=True),
        }
    ),
    "crop_acres": va.DataFrameSchema(
        {
            "site_id": va.Column(int),
            "crop_id": va.Column(float, nullable=True),
            "crop": va.Column(str, nullable=True),
            "crop_year": va.Column(float, nullable=True),
            "acres": va.Column(float, nullable=True),
        }
    ),
    "invoices": va.DataFrameSchema(
        {
            "ag_collect_retail_site_id": va.Column(int),
            "retail_site_name": va.Column(str, nullable=True),
            "retail_site_status": va.Column(str, nullable=True),
            "retail_site_address": va.Column(str, nullable=True),
            "retail_site_city_name": va.Column(str, nullable=True),
            "retail_site_province_name": va.Column(str, nullable=True),
            "retail_site_postal": va.Column(str, nullable=True),
            "ag_collect_retail_house_id": va.Column(float, nullable=True),
            "retail_house_name": va.Column(str, nullable=True),
            "retail_house_status_id": va.Column(float, nullable=True),
            "retail_house_status": va.Column(str, nullable=True),
            "retail_house_address": va.Column(str, nullable=True),
            "retail_house_city_name": va.Column(str, nullable=True),
            "retail_house_province_name": va.Column(str, nullable=True),
            "retail_house_postal": va.Column(str, nullable=True),
            "ag_collect_dist_site_id": va.Column(float, nullable=True),
            "distributor_name": va.Column(str, nullable=True),
            "site_id": va.Column(float, nullable=True),
            "site_name": va.Column(str, nullable=True),
            "site_status_id": va.Column(float, nullable=True),
            "site_status": va.Column(str, nullable=True),
            "site_address": va.Column(str, nullable=True),
            "site_city": va.Column(str, nullable=True),
            "site_province": va.Column(str, nullable=True),
            "site_postal": va.Column(str, nullable=True),
            "house_id": va.Column(float, nullable=True),
            "house_name": va.Column(str, nullable=True),
            "house_status_id": va.Column(float, nullable=True),
            "house_status": va.Column(str, nullable=True),
            "ag_collect_product_id": va.Column(float, nullable=True),
            "product_name": va.Column(str, nullable=True),
            "product_uom": va.Column(str, nullable=True),
            "ag_collect_parent_product_id": va.Column(float, nullable=True),
            "parent_product_name": va.Column(str, nullable=True),
            "parent_product_uom": va.Column(str, nullable=True),
            "brand_id": va.Column(float, nullable=True),
            "brand": va.Column(str, nullable=True),
            "quantity": va.Column(str, nullable=True),
            "parent_product_conversion_factor": va.Column(str, nullable=True),
            "converted_quantity": va.Column(str, nullable=True),
            "acres_per_case": va.Column(str, nullable=True),
            "converted_acres": va.Column(str, nullable=True),
            "total_price": va.Column(str, nullable=True),
            "total_msrp": va.Column(str, nullable=True),
            "total_msdp": va.Column(str, nullable=True),
            "program_year": va.Column(str, nullable=True),
            "invoice_date": va.Column(str, nullable=True),
            "ag_collect_invoice_detail_id": va.Column(float, nullable=True),
            "invoice_number": va.Column(str, nullable=True),
            "invoice_detail_status_id": va.Column(float, nullable=True),
            "invoice_detail_status": va.Column(str, nullable=True),
            "invoice_detail_type_id": va.Column(float, nullable=True),
            "invoice_detail_type": va.Column(str, nullable=True),
            "validated": va.Column(bool, nullable=True, parsers=[parser.parse_boolean]),
            "validated_date": va.Column(str, nullable=True),
            "territory_id": va.Column(str, nullable=True),
            "territory_rep": va.Column(str, nullable=True),
        }
    ),
}
