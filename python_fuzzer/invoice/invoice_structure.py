from datetime import date, time
from typing import Optional

class Invoice():
    # UBLExtensions Optional[
    UBLVersionID: int # identifiers (alle int (undtagen den med numeric)) string giver ikke schema fejl, kun schematron, så kan måske ændres til det 
    CustomizationID: int
    ProfileID: int
    ID: int
    CopyIndicator: Optional[bool]
    UUID: Optional[int]
    IssueDate: date #date type (yyyy-mm-dd)
    IssueTime: Optional[time] #time type (00:00:00)
    InvoiceTypeCode: Optional[str] #code type (example doc has e.g. 380 and DKK, so string to generalize)
    Note: Optional[str] #multiple - list of?
    TaxPointDate: Optional[date]
    DocumentCurrencyCode: str #code
    TaxCurrencyCode: Optional[str] #code
    PricingCurrencyCode: Optional[str] # code
    PaymentCurrencyCode: Optional[str] # code
    PaymentAlternativeCurrencyCode: Optional[str] # code
    AccountingCostCode: Optional[str] #code
    AccountingCost: Optional[str]
    LineCountNumeric: Optional[int] #numeric: int?
    # InvoicePeriod Optional[
    # OrderReference Optional[
    # BillingReference Optional[ - multiple
    # DespatchDocumentReference Optional[ - multiple
    # ReceiptDocumentReference Optional[ - multiple
    # OriginatorDocumentReference Optional[ - multiple
    # ContractDocumentReference Optional[
    # AdditionalDocumentReference Optional[ - multiple
    # Signature Optional[ - multiple
    # AccountingSupplierParty 
    # AccountingCustomerParty 
    # PayeeParty Optional[ 
    # BuyerCustomerParty Optional[
    # SellerSupplierParty Optional[
    # Delivery Optional[ - multiple
    # DeliveryTerms Optional[
    # PaymentMeans Optional[ - multiple
    # PaymentTerms Optional[ - multiple
    # PrepaidPayment Optional[ - multiple
    # AllowanceCharge Optional[ - multiple
    # TaxExchangeRate Optional[
    # PricingExchangeRate Optional[
    # PaymentExchangeRate Optional[
    # PaymentAlternativeExchangeRate Optional[
    # TaxTotal - multiple
    # LegalMonetaryTotal
    # InvoiceLine - multiple