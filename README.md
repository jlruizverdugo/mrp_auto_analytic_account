# mrp_auto_analytic_account
Creates a project with the manufacturing reference and assigns the analytic account when the manufacturing order is confirmed.
# MRP Auto Analytic Account

## Overview
This Odoo 16 module automatically creates a **project** using the manufacturing order reference and assigns an **analytic account** when the manufacturing order is confirmed.  
It helps maintain a consistent link between manufacturing, projects, and analytic accounting for better cost tracking and reporting.

## Features
- Automatically creates a project when a manufacturing order is confirmed.  
- The project name uses the manufacturing order reference.  
- Assigns the corresponding analytic account to the manufacturing order.  
- Improves integration between the Manufacturing and Project applications.  
- Simplifies cost and analytic accounting management for production activities.

## Installation
1. Download or clone this repository into your Odoo addons folder:
Restart your Odoo server.

Activate Developer Mode in Odoo.

Go to Apps → Update Apps List.

Search for MRP Auto Analytic Account and click Install.

Usage
Go to Manufacturing → Manufacturing Orders.

Create a new manufacturing order.

When you confirm the order, the module will:

Create a new Project named after the manufacturing order reference.

Automatically link an Analytic Account to that project and to the manufacturing order.

You can find and manage the created project under Project → Projects.

Compatibility
Odoo 16.0

Depends on: mrp, project, analytic

Author
José Luis Ruiz Verdugo

License
This module is licensed under the LGPL-3 License.
