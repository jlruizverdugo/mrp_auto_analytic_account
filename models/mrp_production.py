from odoo import models, fields, api

class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    # Enlace opcional al proyecto creado
    project_id = fields.Many2one(
        'project.project',
        string='Project',
        readonly=False,
        required=False,
    )

    def action_confirm(self):
        # 1) Confirmar primero para asegurar que la referencia (name) ya esté asignada
        res = super(MrpProduction, self).action_confirm()

        # 2) Crear proyecto con la referencia definitiva y asignar cuenta analítica a la MO
        for production in self:
            # Nombre del proyecto = referencia final de la fabricación
            project_name = production.name or ('Manufacturing %s' % (production.id,))

            # Crear el proyecto si aún no está enlazado
            project = production.project_id
            if not project:
                project = self.env['project.project'].create({'name': project_name})
                production.project_id = project.id

            # Asegurar cuenta analítica en el proyecto
            analytic = getattr(project, 'analytic_account_id', False)
            if not analytic:
                # Crear cuenta analítica con el nombre del proyecto (y misma compañía si aplica)
                create_vals = {'name': project.name}
                if 'company_id' in production._fields and production.company_id:
                    create_vals['company_id'] = production.company_id.id
                analytic = self.env['account.analytic.account'].create(create_vals)

                # Enlazarla al proyecto si el campo existe
                if 'analytic_account_id' in self.env['project.project']._fields:
                    project.write({'analytic_account_id': analytic.id})

            # 3) Escribir la cuenta analítica en la MO (pestaña Varios / Cuenta Analítica)
            if 'analytic_account_id' in production._fields and analytic:
                production.write({'analytic_account_id': analytic.id})

        return res
