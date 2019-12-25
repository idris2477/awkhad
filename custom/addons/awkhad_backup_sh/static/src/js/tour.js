// Copyright 2018 Stanislav Krotov <https://it-projects.info/team/ufaks>
// License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

awkhad.define("awkhad_backup_sh.tour", function (require) {
    "use strict";

    var core = require("web.core");
    var tour = require("web_tour.tour");

    var _t = core._t;

    tour.register("awkhad_backup_sh_tour", {
            url: "/web",
            test: true,
        },
        [
            tour.STEPS.SHOW_APPS_MENU_ITEM,
            {
                trigger: '.o_app[data-menu-xmlid="awkhad_backup_sh.menu_backup_root"]',
                content: _t('Want a better way to <b>manage your databases backups</b>? <i>It starts here.</i>'),
                position: "right",
                edition: 'community'
            }, {
                trigger: '.o_app[data-menu-xmlid="awkhad_backup_sh.menu_backup_root"]',
                content: _t('Want a better way to <b>manage your databases backups</b>? <i>It starts here.</i>'),
                position: "bottom",
                edition: 'enterprise'
            },
            {
                // Check that at least one button in dashboard is visible
                trigger: '.o_dashboard_common .o_inner_box',
                run: function () {
                    // empty
                },
            }
        ]
    );
});