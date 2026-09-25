import { Component, onMounted, onWillStart, onWillUnmount, proxy, useProps } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { Layout } from "@web/search/layout";
import { standardActionServiceProps } from "@web/webclient/actions/action_plugin";


class ParcPresse extends Component {
    static components = { Layout };
    static template = "is_alencon20.parc_presse_template";
    props = useProps(standardActionServiceProps);

    setup() {
        this.orm   = useService("orm");
        this.state = proxy({
            'equipements': {},
        });
        this._interval=null;

        onWillStart(async () => {
            await this.getParcPresse();
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
            //*****************************************************************
        });
        onWillUnmount(() => {
            clearInterval(this._interval);
            this._interval=null;
        });
    }

    async getParcPresse(){
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

registry.category("actions").add("is_alencon.parc_presse_registry", ParcPresse);
