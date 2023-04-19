from datetime import date, time
from typing import Optional, List, Union, Any
from dataclasses import dataclass, fields

@dataclass 
class DeliveryLocation():
    ID: int 
    Description: str #Optional[str] 
    Conditions: str #Optional[str] 
    CountrySubentity: str #Optional[str] 
    CountrySubentityCode: str #Optional[str] # code
    #ValidityPeriod #Optional[
    #Address #Optional[

@dataclass 
class DeliveryTerms():
    ID: int #Optional[int]  
    SpecialTerms: str #Optional[str] 
    LossRiskResponsibilityCode: str #Optional[str] # code
    LossRisk: str #Optional[str]  
    DeliveryLocation: DeliveryLocation #Optional[DeliveryLocation]

@dataclass 
class OtherCommunication():
    ChannelCode: str #Optional[str] #datatype code? (dokumentationen beskriver ikke datatypen for denne klasse)
    Channel: str #Optional[str] #datatype text?
    Value: str #datatype text?

@dataclass 
class Contact():
    ID: int
    Name: str #Optional[str] #datatype: name
    Telephone: str #Optional[str]
    Telefax: str #Optional[str]
    ElectronicMail: str #Optional[str]
    Note: str #Optional[str]
    OtherCommunication: OtherCommunication #Optional[OtherCommunication]

@dataclass 
class PayeeParty():
    WebsiteURI: int #Optional[int]
    LogoReferenceID: int #Optional[int]
    EndpointID: int #Optional[int]
    #PartyIdentification Optional[ #multiple instances possible
    #PartyName Optional[ #multiple instances possible
    #Language Optional[
    #PostalAddress Optional[
    #PhysicalLocation Optional[
    #PartyTaxScheme Optional[ #multiple instances possible
    #PartyLegalEntity
    Contact: Contact #Optional[Contact]
    #Person Optional[

@dataclass 
class Party():
    WebsiteURI: int #Optional[int]
    LogoReferenceID: int #Optional[int]
    EndpointID: int #optional for BuyerCustomerParty, and SellerSupplierParty
    #PartyIdentification Optional[ #multiple instances possible
    #PartyName Optional[ #multiple instances possible
    #Language Optional[
    #PostalAddress Optional[
    #PhysicalLocation Optional[
    #PartyTaxScheme Optional[ #multiple instances possible
    #PartyLegalEntity
    Contact: Contact #(Optional for AccountingSupplierParty, BuyerCustomerParty, and SellerSupplierParty, but mandatory for AccountingCustomerParty)
    #Person Optional[


@dataclass 
class Delivery():
    ID: int #Optional[int]
    Quantity: float #Optional[float] #datatype: quantity
    MinimumQuantity: float #Optional[float] #datatype: quantity
    MaximumQuantity: float #Optional[float] #datatype: quantity
    ActualDeliveryDate: date #Optional[date]
    ActualDeliveryTime: time #Optional[time]
    LatestDeliveryDate: date #Optional[date]
    LatestDeliveryTime: time #Optional[time]
    TrackingID: int #Optional[str]
    #DeliveryLocation #Optional[
    #RequestedDeliveryPeriod #Optional[
    #DeliveryParty #Optional[
    #Despatch #Optional[

@dataclass 
class SellerSupplierParty():
    CustomerAssignedAccountID: int #Optional[int]
    AdditionalAccountID: int #Optional[List[int]] #multiple instances possible
    Party: Party
    #DespatchContact: Optional[
    #AccountingContact: Optional[
    #SellerContact: Optional[

@dataclass 
class BuyerCustomerParty():
    CustomerAssignedAccountID: int #Optional[int]
    SupplierAssignedAccountID: int #Optional[List[int]] #multiple instances possible
    AdditionalAccountID: int #Optional[List[int]] #multiple instances possible
    Party: Party
    #DeliveryContact: Optional[
    #AccountingContact: Optional[
    #BuyerContact: Optional[

@dataclass 
class AccountingCustomerParty():
    CustomerAssignedAccountID: int #Optional[int]
    SupplierAssignedAccountID: int #Optional[int]
    AdditionalAccountID: int #Optional[List[int]] #multiple instances possible
    Party: Party
    #DespatchContact: Optional[
    #AccountingContact: Optional[
    #SellerContact: Optional[

@dataclass 
class AccountingSupplierParty():
    CustomerAssignedAccountID: int #Optional[int]
    AdditionalAccountID: int #Optional[List[int]] #multiple instances possible
    Party: Party
    #DeliveryContact: Optional[
    #AccountingContact: Optional[
    #BuyerContact: Optional[

@dataclass 
class Attachment():
    EmbeddedDocumentBinaryObject: bytes #Optional[bytes] # binary type
    #ExternalReference Optional[

@dataclass 
class DocumentReference():
    ID: int
    CopyIndicator: bool #Optional[bool]
    UUID: int #Optional[int]
    IssueDate: date #Optional[date] #date type (yyyy-mm-dd)
    XPath: str #Optional[List[str]] #multiple instances possible
    Attachment: Attachment #Optional[Attachment]

@dataclass 
class ContractDocumentReference(DocumentReference):
    pass

@dataclass 
class OriginatorDocumentReference(DocumentReference):
    pass

@dataclass 
class ReceiptDocumentReference(DocumentReference):
    pass

@dataclass 
class DespatchDocumentReference(DocumentReference):
    pass

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
    InvoiceDocumentReference: InvoiceDocumentReference #Optional[InvoiceDocumentReference]
    SelfBilledInvoiceDocumentReference: SelfBilledInvoiceDocumentReference #Optional[SelfBilledInvoiceDocumentReference]
    CreditNoteDocumentReference: CreditNoteDocumentReference #Optional[CreditNoteDocumentReference]
    SelfBilledCreditNoteDocumentReference: SelfBilledCreditNoteDocumentReference #Optional[SelfBilledCreditNoteDocumentReference]
    ReminderDocumentReference: ReminderDocumentReference #Optional[ReminderDocumentReference]

@dataclass 
class OrderReference():
    ID: int
    CopyIndicator: bool #Optional[bool]
    UUID: int #Optional[int]
    IssueDate: date #Optional[date] #date type (yyyy-mm-dd)
    IssueTime: time #Optional[time] #time type (00:00:00)
    SalesOrderID: int #Optional[int]
    CustomerReference: str #Optional[str]
    DocumentReference: DocumentReference #Optional[DocumentReference]

@dataclass #provide automatic generation of __init__(), among other things
class Invoice():
    # UBLExtensions Optional[
    UBLVersionID: int # identifiers (alle int er indentifiers, undtagen den med numeric) strings giver ikke schema fejl, kun schematron, så kan måske ændres til det 
    CustomizationID: int
    ProfileID: int
    ID: int
    CopyIndicator: bool #Optional[bool]
    UUID: int #Optional[int]
    IssueDate: date #date type (yyyy-mm-dd)
    IssueTime: time #Optional[time] #time type (00:00:00)
    InvoiceTypeCode: str #Optional[str] #code type (example doc has e.g. 380 and DKK, so string to generalize)
    Note: str #Optional[List[str]] #multiple instances possible - list of?
    TaxPointDate: date #Optional[date]
    DocumentCurrencyCode: str #code
    TaxCurrencyCode: str #Optional[str] #code
    PricingCurrencyCode: str #Optional[str] # code
    PaymentCurrencyCode: str #Optional[str] # code
    PaymentAlternativeCurrencyCode: str #Optional[str] # code
    AccountingCostCode: str #Optional[str] #code
    AccountingCost: str #Optional[str]
    LineCountNumeric: int #Optional[int] #numeric: int?
    # InvoicePeriod Optional[
    OrderReference: OrderReference #Optional[OrderReference]
    BillingReference: BillingReference #Optional[List[BillingReference]] # multiple instances possible
    DespatchDocumentReference: DespatchDocumentReference #Optional[List[DespatchDocumentReference]] # multiple instances possible
    ReceiptDocumentReference: ReceiptDocumentReference #Optional[List[ReceiptDocumentReference]] # multiple instances possible
    OriginatorDocumentReference: OriginatorDocumentReference #Optional[List[OriginatorDocumentReference]] # multiple instances possible
    ContractDocumentReference: ContractDocumentReference #Optional[ContractDocumentReference]
    # AdditionalDocumentReference Optional[ - multiple instances possible
    # Signature Optional[ - multiple instances possible
    AccountingSupplierParty: AccountingSupplierParty
    AccountingCustomerParty: AccountingCustomerParty
    PayeeParty: PayeeParty #Optional[PayeeParty]
    BuyerCustomerParty: BuyerCustomerParty #Optional[BuyerCustomerParty]
    SellerSupplierParty: SellerSupplierParty #Optional[SellerSupplierParty]
    Delivery: Delivery #Optional[ - multiple instances possible
    DeliveryTerms: DeliveryTerms #Optional[
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
