from policyengine_us.model_api import *


class ar_medical_expense_deduction(Variable):
    value_type = float
    entity = TaxUnit
    label = "Arkansas medical and dental expense deduction"
    unit = USD
    definition_period = YEAR
    reference = "https://www.dfa.arkansas.gov/images/uploads/incomeTaxOffice/2022_AR1000F_and_AR1000NR_Instructions.pdf#page=21"
    defined_for = StateCode.AR

    def formula(tax_unit, period, parameters):
        year = period.start.year
        agi = tax_unit("ar_agi", period)
        # Arkansas applies the federal medical expense floor rate which was established in 2013
        if year >= 2017:
            instant_str = f"2017-01-01"
        else:
            instant_str = f"2013-01-01"
        p = parameters(instant_str).gov.irs.deductions.itemized.medical
        medical_expenses = add(tax_unit, period, ["medical_expense"])
        return max_(
            0,
            medical_expenses - p.floor * agi,
        )
