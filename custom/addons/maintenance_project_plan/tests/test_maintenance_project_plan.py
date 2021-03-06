# Copyright 2019 Solvos Consultoría Informática (<http://www.solvos.es>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

import awkhad.tests.common as test_common


class TestMaintenanceProjectPlan(test_common.TransactionCase):

    def setUp(self):
        super().setUp()

        self.cron = self.env.ref('maintenance.maintenance_requests_cron')

        self.maintenance_kind_weekly = \
            self.env.ref('maintenance_plan.maintenance_kind_weekly')

        self.monitor1 = self.env.ref('maintenance.equipment_monitor1')
        self.monitor1.maintenance_plan_ids = [(0, 0, {
            'maintenance_kind_id': self.maintenance_kind_weekly.id,
            'period': 7,
            'duration': 1,
            'project_id':
                self.env.ref('maintenance_project.project_project_1').id,
            'task_id': self.env.ref('maintenance_project.project_task_11').id
        })]

    def test_prepare_request_from_plan(self):
        plans = self.env['maintenance.plan'].search(
            [('project_id', '!=', False)])
        for plan in plans:
            data = plan.equipment_id._prepare_request_from_plan(plan)
            self.assertEqual(data['project_id'], plan.project_id.id)
            self.assertEqual(data.get('task_id', False), plan.task_id.id)

    def test_plan_onchange_project(self):
        plan1 = self.env['maintenance.plan'].new({
            'equipment_id': self.env.ref(
                'maintenance_plan.maintenance_plan_monthly_monitor4').id,
            'maintenance_kind_id': self.maintenance_kind_weekly.id,
            'period': 7,
            'duration': 1,
            'project_id':
                self.env.ref('maintenance_project.project_project_1').id,
            'task_id':
                self.env.ref('maintenance_project.project_task_11').id})
        self.assertEqual(plan1.project_id,
                         self.env.ref('maintenance_project.project_project_1'))
        self.assertEqual(plan1.task_id,
                         self.env.ref('maintenance_project.project_task_11'))
        plan1.project_id = False
        ctx1 = plan1.onchange_project_id()
        self.assertFalse(plan1.task_id)
        self.assertFalse(ctx1['domain']['task_id'][0][2])

        plan1.project_id = self.env.ref(
            'maintenance_project.project_project_1')
        ctx2 = plan1.onchange_project_id()
        self.assertFalse(plan1.task_id)
        self.assertEqual(
            ctx2['domain']['task_id'][0][2],
            self.env.ref('maintenance_project.project_project_1').id)
