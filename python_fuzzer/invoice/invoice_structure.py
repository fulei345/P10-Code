from datetime import date, time

class Invoice():
    UBLVersionID: int # identifiers (alle int (undtagen den med numeric)) string giver ikke schema fejl, kun schematron, så kan måske ændres til det 
    CustomizationID: int
    ProfileID: int
    ID: int
    CopyIndicator: bool
    UUID: int
    IssueDate: date #date type (yyyy-mm-dd)
    IssueTime: time #time type (00:00:00)
    InvoiceTypeCode: str #code type (example doc has e.g. 380 and DKK, so string to generalize)
    Note: str
    TaxPointDate: date
    DocumentCurrencyCode: str #code
    TaxCurrencyCode: str #code
    PricingCurrencyCode: str # code
    PaymentCurrencyCode: str # code
    PaymentAlternativeCurrencyCode: str # code
    AccountingCostCode: str #code
    AccountingCost: str
    LineCountNumeric: int #numeric: int?
    # UBLExtensions
    # InvoicePeriod
    # OrderReference
    # BillingReference
    # DespatchDocumentReference
    # ReceiptDocumentReference
    # OriginatorDocumentReference
    # ContractDocumentReference
    # AdditionalDocumentReference 
    # Signature 
    # AccountingSupplierParty
    # AccountingCustomerParty
    # PayeeParty
    # BuyerCustomerParty
    # SellerSupplierParty
    # Delivery
    # DeliveryTerms
    # PaymentMeans
    # PaymentTerms
    # PrepaidPayment
    # AllowanceCharge
    # TaxExchangeRate
    # PricingExchangeRate
    # PaymentExchangeRate
    # PaymentAlternativeExchangeRate
    # TaxTotal
    # LegalMonetaryTotal
    # InvoiceLine