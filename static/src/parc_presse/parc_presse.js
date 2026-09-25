/** @odoo-module **/
import { registry } from "@web/core/registry";
import { Layout } from "@web/search/layout";
import { getDefaultConfig } from "@web/views/view";
import { useService } from "@web/core/utils/hooks";

const { Component, useSubEnv, useState, onWillStart,onMounted,onWillUnmount } = owl;


class ParcPresse extends Component {
    setup() {
        this.user_id = useService("user").context.uid;
        this.action  = useService("action");
        this.orm     = useService("orm");
        this.state   = useState({
            'equipements': {},
        });
        this._interval=null;

        useSubEnv({
            config: {
                ...getDefaultConfig(),
                ...this.env.config,
            },
        });
        this.display = {
            controlPanel: { "top-right": false, "bottom-right": false },
        };
        onWillStart(async () => {
            this.getParcPresse();
        });

        onMounted(() => {
            //Rafraichissement toutes les 60s *********************************
            if (!this._interval) {
                this._interval = setInterval(() => {
                    if (this._interval){
                        this.getParcPresse();
                    }
                }, 1000 * 60);
            }
            //***************************************************************** */
        });
        onWillUnmount(() => {
            clearInterval(this._interval);
            this._interval=null;
        });
    } 

    OKclick(ev) {
        this.getParcPresse(true);
    }


    async getParcPresse(ok=false){
        var res = await this.orm.call("is.equipement", 'get_parc_presse', [false]);
        this.state.equipements   = res.equipements;
        this.state.now_date      = res.now_date;
        this.state.now_heure     = res.now_heure;
        this.state.tx_cycle_parc = res.tx_cycle_parc;
        this.state.tx_fct_parc   = res.tx_fct_parc;
        this.state.tx_rebut_parc = res.tx_rebut_parc;
        this.state.style_tx_cycle_parc = res.style_tx_cycle_parc;
        this.state.style_tx_fct_parc   = res.style_tx_fct_parc;
        this.state.style_tx_rebut_parc = res.style_tx_rebut_parc;
     }
}


ParcPresse.components = { Layout };
ParcPresse.template = "is_alencon.parc_presse_template";
registry.category("actions").add("is_alencon.parc_presse_registry", ParcPresse);




