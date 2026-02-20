CA_rates = [14, 20.5, 26, 29, 33]
CA_money = [0, 58523, 117045, 181440, 258482]
NL_rates = [8.7, 14.5, 15.8, 17.8, 19.8, 20.8, 21.3, 21.8]
NL_money = [0, 44678, 89354, 159528, 223340, 285319, 570638, 1141275]
PE_rates = [9.5, 13.47, 16.6, 17.62, 19]
PE_money = [0, 33928, 65820, 106890, 142250]
NS_rates = [8.79, 14.95, 16.67, 17.5, 21]
NS_money = [0, 30995, 61991, 97417, 157124]
NB_rates = [9.4, 14, 16, 19.5]
NB_money = [0, 52333, 104666, 193861]
QC_rates = [14, 19, 24, 25.75]
QC_money = [0, 54345, 108680, 132245]
ON_rates = [5.05, 9.15, 11.16, 12.16, 13.16]
ON_money = [0, 53891, 107785, 150000, 220000]
MB_rates = [10.8, 12.75, 17.4]
MB_money = [0, 47000, 100000]
SK_rates = [10.5, 12.5, 14.5]
SK_money = [0, 54532, 155805]
AB_rates = [8, 10, 12, 13, 14, 15]
AB_money = [0, 61200, 154259, 185111, 246813, 370220]
BC_rates = [5.06, 7.7, 10.5, 12.29, 14.7, 16.8, 20.5]
BC_money = [0, 50363, 100728, 115648, 140430, 190405, 265545]
YT_rates = [6.4, 9, 10.9, 12.8, 15]
YT_money = [0, 58523, 117045, 181440, 500000]
NT_rates = [5.9, 8.6, 12.2, 14.05]
NT_money = [0, 53003, 106009, 172346]
NU_rates = [4, 7, 9, 11.5]
NU_money = [0, 55801, 111602, 181439]
ProvinceMap = {
    "ontario": (ON_rates, ON_money),
    "quebec": (QC_rates, QC_money),
    "nova scotia": (NS_rates, NS_money),
    "new brunswick": (NB_rates, NB_money),
    "manitoba": (MB_rates, MB_money),
    "british columbia": (BC_rates, BC_money),
    "prince edward island": (PE_rates, PE_money),
    "saskatchewan": (SK_rates, SK_money),
    "alberta": (AB_rates, AB_money),
    "newfoundland and labrador": (NL_rates, NL_money),
    "yukon": (YT_rates, YT_money),
    "northwest territories": (NT_rates, NT_money),
    "nunavut": (NU_rates, NU_money)
}
def CalculateTax(Income, Rates, Money):
    TotalTax = 0
    for i in range(len(Rates)):
        Lower = Money[i]
        Rate = Rates[i] / 100
        
        if i + 1 < len(Money):
            Upper = Money[i+1]
        else:
            Upper = float("inf")

        if Income > Lower:
            TaxableAmount = min(Income, Upper) - Lower
            TotalTax += TaxableAmount * Rate
        else:
            break
            
    return TotalTax

print("How much taxable income do you have?")
income = 0
IncomeTruth = False
while IncomeTruth == False:
    try:
        income = int(input())
        IncomeTruth = True
    except:
        print("invalid format")
ProvinceTruth = False
print("What Province do you reside in")
while ProvinceTruth == False:
    Province = str(input()).strip().lower()
    if Province in ProvinceMap:
        ProvinceRate, ProvinceMoney = ProvinceMap[Province]
        ProvinceTruth = True
    else:
        print("Invalid Format")
FederalTax = CalculateTax(income, CA_rates, CA_money)
ProvincialTax = CalculateTax(income, ProvinceRate, ProvinceMoney)
TotalDue = FederalTax + ProvincialTax
EffectiveRate = (TotalDue / income) * 100
print(f"Federal Tax: ${FederalTax:,.2f}")
print(f"Provincial Tax: ${ProvincialTax:,.2f}")
print(f"Total Tax: ${TotalDue:,.2f}")
print(f"Effective Tax Rate: {EffectiveRate:.2f}%")
