from datetime import date, time
from typing import Optional, List
from dataclasses import dataclass

@dataclass 
class Attachment():
    EmbeddedDocumentBinaryObject: Optional[bytes] # binary type
    #ExternalReference Optional[

@dataclass 
class DocumentReference():
    ID: int
    CopyIndicator: Optional[bool]
    UUID: Optional[int]
    IssueDate: Optional[date] #date type (yyyy-mm-dd)
    XPath: Optional[List[str]] #multiple instances possible
    Attachment: Optional[Attachment]

@dataclass 
class ReminderDocumentReference(DocumentReference):
    pass

@dataclass 
class SelfBilledCreditNoteDocumentReference(DocumentReference):
    pass

@dataclass 
class CreditNoteDocumentReference(DocumentReference):
    pass

@dataclass 
class SelfBilledInvoiceDocumentReference(DocumentReference):
    pass

@dataclass 
class InvoiceDocumentReference(DocumentReference):
    pass
    
@dataclass 
class BillingReference():
    InvoiceDocumentReference: Optional[InvoiceDocumentReference]
    SelfBilledInvoiceDocumentReference: Optional[SelfBilledInvoiceDocumentReference]
    CreditNoteDocumentReference: Optional[CreditNoteDocumentReference]
    SelfBilledCreditNoteDocumentReference: Optional[SelfBilledCreditNoteDocumentReference]
    ReminderDocumentReference: Optional[ReminderDocumentReference]

@dataclass 
class OrderReference():
    ID: int
    CopyIndicator: Optional[bool]
    UUID: Optional[int]
    IssueDate: Optional[date] #date type (yyyy-mm-dd)
    IssueTime: Optional[time] #time type (00:00:00)
    SalesOrderID: Optional[int]
    CustomerReference: Optional[str]
    DocumentReference: Optional[DocumentReference]

@dataclass #provide automatic generation of __init__(), among other things
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
    Note: Optional[List[str]] #multiple instances possible - list of?
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
    OrderReference: Optional[OrderReference]
    BillingReference: Optional[List[BillingReference]] # multiple instances possible
    # DespatchDocumentReference Optional[ - multiple instances possible
    # ReceiptDocumentReference Optional[ - multiple instances possible
    # OriginatorDocumentReference Optional[ - multiple instances possible
    # ContractDocumentReference Optional[
    # AdditionalDocumentReference Optional[ - multiple instances possible
    # Signature Optional[ - multiple instances possible
    # AccountingSupplierParty 
    # AccountingCustomerParty 
    # PayeeParty Optional[ 
    # BuyerCustomerParty Optional[
    # SellerSupplierParty Optional[
    # Delivery Optional[ - multiple instances possible
    # DeliveryTerms Optional[
    # PaymentMeans Optional[ - multiple instances possible
    # PaymentTerms Optional[ - multiple instances possible
    # PrepaidPayment Optional[ - multiple instances possible
    # AllowanceCharge Optional[ - multiple instances possible
    # TaxExchangeRate Optional[
    # PricingExchangeRate Optional[
    # PaymentExchangeRate Optional[
    # PaymentAlternativeExchangeRate Optional[
    # TaxTotal - multiple instances possible
    # LegalMonetaryTotal
    # InvoiceLine - multiple instances possible