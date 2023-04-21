from datetime import date, time
from typing import Optional, List, Union, Any
from dataclasses import dataclass, fields


@dataclass 
class LegalMonetaryTotal(): #!
    LineExtensionAmount: float #Optional[float] #datatype: amount
    TaxExclusiveAmount: float #Optional[float] #datatype: amount
    TaxInclusiveAmount: float #Optional[float] #datatype: amount
    AllowanceTotalAmount: float #Optional[float] #datatype: amount
    ChargeTotalAmount: float #Optional[float] #datatype: amount
    PrepaidAmount: float #Optional[float] #datatype: amount
    PayableRoundingAmount: float #Optional[float] #datatype: amount
    PayableAmount: float #datatype: amount
    PayableAlternativeAmount: float #Optional[float] #datatype: amount

@dataclass 
class TaxTotal(): #!
    TaxAmount: float #datatype: amount
    RoundingAmount: float #Optional[float] #datatype: amount
    TaxEvidenceIndicator: bool #Optional[bool] 
    TaxIncludedIndicator: bool #Optional[bool] 
    # TaxSubtotal: #Optional[] #multiple instances possible

@dataclass 
class PaymentMeans():
    ID: int #Optional[int]
    PaymentMeansCode: str #datatype: code
    PaymentDueDate: date #Optional[date]
    PaymentChannelCode: str #Optional[str] #datatype: code
    InstructionID: int #Optional[int]
    InstructionNote: str #Optional[str] 
    PaymentID: int #Optional[int] #multiple instances possible
    #CardAccount #Optional[ 
    #PayerFinancialAccount #Optional[ 
    #PayeeFinancialAccount #Optional[ 
    #CreditAccount #Optional[ 
    

@dataclass 
class AllowanceCharge(): #!
    ID: int #Optional[int]
    ChargeIndicator: bool 
    AllowanceChargeReasonCode: str #Optional[str] #datatype: code
    AllowanceChargeReason: str #Optional[str]
    MultiplierFactorNumeric: int #Optional[int] #numeric
    PrepaidIndicator: bool #Optional[bool]
    SequenceNumeric: int #Optional[int] #numeric
    Amount: float #datatype: amount
    BaseAmount: float #Optional[float] #datatype: amount
    AccountingCostCode: str #Optional[str] #datatype: code
    AccountingCost: str #Optional[str] 
    #TaxCategory #Optional[] #multiple instances possible
    TaxTotal: TaxTotal #Optional[] 
    PaymentMeans: PaymentMeans #Optional[] #multiple instances possible

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
class OtherCommunication(): #!
    ChannelCode: str #Optional[str] #datatype code 
    Channel: str #Optional[str] #datatype text
    Value: str #datatype text

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
class PartyLegalEntity(): #!
    RegistrationName: str #Optional[str] # name
    CompanyID: int #Optional[int]
    CompanyTypeCode: str #Optional[str] # code
    CompanyLiquidationStatusCode: str #Optional[str] # code
    RegistrationDate: date #Optional[date]
    RegistrationExpirationDate: date #Optional[date]
    CorporateStockAmount: float #Optional[float] #datatype: amount
    #RegistrationAddress Optional[
    #CorporateRegistrationScheme Optional[
    #StakeholderParty Optional[ #multiple instances possible
    #CompanyDossierDocumentReference Optional[


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
    PartyLegalEntity: PartyLegalEntity
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
    PartyLegalEntity: PartyLegalEntity
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
class ForeignExchangeContract():
    ID: int
    IssueDate: date #Optional[date] 
    IssueTime: time #Optional[time]
    ContractTypeCode: str #Optional[str] # code
    ContractType: str #Optional[str]
    #ValidityPeriod #Optional[ValidityPeriod]
    ContractDocumentReference: ContractDocumentReference #Optional[ContractDocumentReference]

@dataclass 
class TaxExchangeRate():
    SourceCurrencyCode: str # code 
    SourceCurrencyBaseRate: int #Optional[int] #rate
    TargetCurrencyCode: str # code
    TargetCurrencyBaseRate: int #Optional[int] #rate
    ExchangeMarketID: int #Optional[int]
    CalculationRate: int #Optional[int] #rate
    MathematicOperatorCode: str #Optional[str] # code
    Date: date #Optional[date]
    ForeignExchangeContract: ForeignExchangeContract #Optional[ForeignExchangeContract]

@dataclass 
class PaymentAlternativeExchangeRate(TaxExchangeRate):
    pass

@dataclass 
class PaymentExchangeRate(TaxExchangeRate):
    pass

@dataclass 
class PricingExchangeRate(TaxExchangeRate):
    pass

@dataclass 
class BillingReference():
    InvoiceDocumentReference: InvoiceDocumentReference #Optional[InvoiceDocumentReference]
    SelfBilledInvoiceDocumentReference: SelfBilledInvoiceDocumentReference #Optional[SelfBilledInvoiceDocumentReference]
    CreditNoteDocumentReference: CreditNoteDocumentReference #Optional[CreditNoteDocumentReference]
    SelfBilledCreditNoteDocumentReference: SelfBilledCreditNoteDocumentReference #Optional[SelfBilledCreditNoteDocumentReference]
    ReminderDocumentReference: ReminderDocumentReference #Optional[ReminderDocumentReference]

@dataclass 
class BuyersItemIdentification():
    ID: int
    ExtendedID: int #Optional[int]
    #IssuerParty #Optional[

@dataclass 
class SellersItemIdentification():
    ID: int
    ExtendedID: int #Optional[int]
    #PhysicalAttribute #Optional[List[]] #multiple instances possible
    #MeasurementDimension #Optional[List[]] #multiple instances possible
    #IssuerParty #Optional[

@dataclass 
class ManufacturersItemIdentification(BuyersItemIdentification):
    pass

@dataclass 
class StandardItemIdentification(BuyersItemIdentification):
    pass

@dataclass 
class CatalogueItemIdentification(BuyersItemIdentification):
    pass

@dataclass 
class AdditionalItemIdentification(BuyersItemIdentification):
    pass

@dataclass 
class CatalogueDocumentReference(DocumentReference):
    pass

@dataclass 
class Price(): #!
    PriceAmount: float #datatype: amount
    BaseQuantity: float #Optional[float] #datatype: quantity 
    PriceChangeReason: str #Optional[str] #multiple instances possible
    PriceTypeCode: str #Optional[str] # code
    PriceType: str #Optional[str] 
    OrderableUnitFactorRate: int #Optional[int] #rate
    # ValidityPeriod: #Optional[] #multiple instances possible
    # PriceList #Optional[ 
    AllowanceCharge: AllowanceCharge #Optional[ #multiple instances possible
    PricingExchangeRate: PricingExchangeRate

@dataclass 
class Item():
    Description: str #Optional[List[str]] #multiple instances possible
    PackQuantity: float #Optional[float] #datatype: quantity
    PackSizeNumeric: int #Optional[int] #numeric
    CatalogueIndicator: bool #Optional[bool]
    Name: str # name
    HazardousRiskIndicator: bool #Optional[bool]
    AdditionalInformation: str #Optional[str]
    Keyword: str #Optional[str]
    BrandName: str #Optional[str] # name
    ModelName: str #Optional[str] # name
    BuyersItemIdentification: BuyersItemIdentification #Optional[BuyersItemIdentification]
    SellersItemIdentification: SellersItemIdentification #Optional[SellersItemIdentification]
    ManufacturersItemIdentification: ManufacturersItemIdentification #Optional[ManufacturersItemIdentification]
    StandardItemIdentification: StandardItemIdentification #Optional[StandardItemIdentification]
    CatalogueItemIdentification: CatalogueItemIdentification #Optional[CatalogueItemIdentification]
    AdditionalItemIdentification: AdditionalItemIdentification #Optional[AdditionalItemIdentification]
    CatalogueDocumentReference: CatalogueDocumentReference #Optional[CatalogueDocumentReference]
    #ItemSpecificationDocumentReference #Optional[
    #OriginCountry #Optional[
    #CommodityClassification #Optional[List[]] #multiple instances possible
    #TransactionConditions #Optional[List[]] #multiple instances possible
    #HazardousItem #Optional[List[]] #multiple instances possible
    #ClassifiedTaxCategory #Optional[List[]] #multiple instances possible
    #AdditionalItemProperty #Optional[List[]] #multiple instances possible
    #ManufacturerParty #Optional[List[]] #multiple instances possible
    #InformationContentProviderParty #Optional[
    #OriginAddress #Optional[
    #ItemInstance #Optional[List[]] #multiple instances possible

@dataclass 
class OrderReference():
    ID: int
    SalesOrderID: int #Optional[int]
    CopyIndicator: bool #Optional[bool]
    UUID: int #Optional[int]
    IssueDate: date #Optional[date] #date type (yyyy-mm-dd)
    IssueTime: time #Optional[time] #time type (00:00:00)
    SalesOrderID: int #Optional[int]
    CustomerReference: str #Optional[str]
    DocumentReference: DocumentReference #Optional[DocumentReference]

@dataclass 
class OrderLineReference():
    LineID: int
    SalesOrderLineID: int #Optional[int]
    UUID: int #Optional[int]
    LineStatusCode: str #Optional[str] #datatype: code
    OrderReference: OrderReference #Optional[OrderReference]

@dataclass 
class InvoiceLine():
    ID: int 
    UUID: int #Optional[int]
    Note: str #Optional[str] 
    InvoicedQuantity: float #datatype: quantity
    LineExtensionAmount: float #datatype: amount
    TaxPointDate: date #Optional[date]
    AccountingCostCode: str #Optional[str] #datatype: code
    AccountingCost: str #Optional[str]
    FreeOfChargeIndicator: bool #Optional[bool]
    OrderLineReference: OrderLineReference #Optional[OrderLineReference]
    #DespatchLineReference #Optional[ #multiple instances possible
    #ReceiptLineReference #Optional[ #multiple instances possible
    BillingReference: BillingReference #Optional[List[BillingReference]] #multiple instances possible
    #PricingReference #Optional[ 
    DocumentReference: DocumentReference #Optional[List[DocumentReference]] #multiple instances possible
    #OriginatorParty #Optional[ 
    Delivery: Delivery #Optional[List[Delivery]] #multiple instances possible
    AllowanceCharge: AllowanceCharge #Optional[ #multiple instances possible
    TaxTotal: TaxTotal #multiple instances possible
    Item: Item 
    Price: Price

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
    PaymentMeans: PaymentMeans #Optional[ - multiple instances possible
    # PaymentTerms Optional[ - multiple instances possible
    # PrepaidPayment Optional[ - multiple instances possible
    AllowanceCharge: AllowanceCharge #Optional[ - multiple instances possible
    TaxExchangeRate: TaxExchangeRate #Optional[TaxExchangeRate]
    PricingExchangeRate: PricingExchangeRate #Optional[PricingExchangeRate]
    PaymentExchangeRate: PaymentExchangeRate #Optional[PaymentExchangeRate]
    PaymentAlternativeExchangeRate: PaymentAlternativeExchangeRate #Optional[PaymentAlternativeExchangeRate]
    TaxTotal: TaxTotal # - multiple instances possible
    LegalMonetaryTotal: LegalMonetaryTotal
    InvoiceLine: InvoiceLine # - multiple instances possible
