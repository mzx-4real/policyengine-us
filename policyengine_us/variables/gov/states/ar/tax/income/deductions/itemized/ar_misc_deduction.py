from policyengine_us.model_api import *


class ar_misc_deduction(Variable):
    value_type = float
    entity = TaxUnit
    label = "Arkansas miscellaneous deduction"
    unit = USD
    definition_period = YEAR
    reference = "https://www.dfa.arkansas.gov/images/uploads/incomeTaxOffice/AR1075_2022.pdf#page=1"
    defined_for = StateCode.AR

    def formula(tax_unit, period, parameters):
        p = parameters(period).gov.irs.deductions.itemized.misc
        misc_ded = tax_unit("misc_deduction", period)
        agi = tax_unit("ar_agi", period)
        return max_(
            0,
            misc_ded - p.floor * agi,
        )
