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
class PaymentTerms():
    ID: str #Optional[int]
    PaymentMeansID: str #Optional[int] #multiple instances possible
    PrepaidPaymentReferenceID: str #Optional[int]
    Note: str #Optional[str] #multiple instances possible
    ReferenceEventCode: str #Optional[str] #datatype: code
    SettlementDiscountPercent: str #Optional[str] #Percent Type
    PenaltySurchargePercent: str #Optional[str] #Percent Type
    PaymentPercent: str #Optional[str] #Percent Type
    Amount: float #Optional[float] #datatype: amount
    SettlementDiscountAmount: float #Optional[float] #datatype: amount
    PenaltyAmount: float #Optional[float] #datatype: amount
    PaymentDueDate: date #Optional[date]
    InstallmentDueDate: date #Optional[date]
    #SettlementPeriod
    #PenaltyPeriod
    #TradeFinancing

@dataclass 
class PaymentMeans():
    ID: str #Optional[int]
    PaymentMeansCode: str #datatype: code
    PaymentDueDate: date #Optional[date]
    PaymentChannelCode: str #Optional[str] #datatype: code
    InstructionID: str #Optional[int]
    InstructionNote: str #Optional[str] 
    PaymentID: str #Optional[int] #multiple instances possible
    #CardAccount #Optional[ 
    #PayerFinancialAccount #Optional[ 
    #PayeeFinancialAccount #Optional[ 
    #CreditAccount #Optional[ 
    

@dataclass 
class AllowanceCharge(): #!
    ID: str #Optional[int]
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
class Address():
    ID: str #Optional[str]
    AddressTypeCode: str #Optional[str] # code
    AddressFormatCode: str #Optional[str] # code
    Postbox: str #Optional[str] 
    Floor: str #Optional[str]
    Room: str #Optional[str]
    StreetName: str #Optional[str] # name
    AdditionalStreetName: str #Optional[str] # name
    BlockName: str #Optional[str] # name
    BuildingName: str #Optional[str] # name
    BuildingNumber: str #Optional[str]
    InhouseMail: str #Optional[str]
    Department: str #Optional[str]
    MarkAttention: str #Optional[str]
    MarkCare: str #Optional[str]
    PlotIdentification: str #Optional[str]
    CitySubdivisionName: str #Optional[str] # name
    CityName: str #Optional[str] # name
    PostalZone: str #Optional[str]
    CountrySubentity: str #Optional[str]
    CountrySubentityCode: str #Optional[str] # code
    Region: str #Optional[str] 
    District: str #Optional[str]
    TimezoneOffset: str #Optional[str]
    #AddressLine #Optional[ #multiple instances possible
    Country: Country #Optional[Country
    #LocationCoordinate #Optional[

@dataclass 
class PostalAddress(Address):
    pass

@dataclass 
class RegistrationAddress(Address):
    pass

@dataclass 
class JurisdictionRegionAddress(Address):
    pass

@dataclass 
class OriginAddress(Address):
    pass

@dataclass 
class RegistrationAddress(Address):
    pass

@dataclass 
class DeliveryLocation():
    ID: str 
    Description: str #Optional[str] 
    Conditions: str #Optional[str] 
    CountrySubentity: str #Optional[str] 
    CountrySubentityCode: str #Optional[str] # code
    #ValidityPeriod #Optional[
    Address: Address #Optional[

@dataclass 
class DeliveryTerms():
    ID: str #Optional[int]  
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
    CompanyID: str #Optional[int]
    CompanyTypeCode: str #Optional[str] # code
    CompanyLiquidationStatusCode: str #Optional[str] # code
    RegistrationDate: date #Optional[date]
    RegistrationExpirationDate: date #Optional[date]
    CorporateStockAmount: float #Optional[float] #datatype: amount
    RegistrationAddress: RegistrationAddress #Optional[
    #CorporateRegistrationScheme Optional[
    #StakeholderParty Optional[ #multiple instances possible
    #CompanyDossierDocumentReference Optional[

@dataclass 
class Country():
    IdentificationCode: str #Optional[str] # code
    Name: str #Optional[str]

@dataclass 
class TaxScheme():
    ID: str #Optional[str]
    Name: str #Optional[str] # name
    TaxTypeCode: str #Optional[str] # code
    CurrencyCode: str #Optional[str] # code
    JurisdictionRegionAddress: JurisdictionRegionAddress #Optional[ #multiple instances possible

@dataclass 
class PartyTaxScheme():
    RegistrationName: str #Optional[str] # name
    CompanyID: str #Optional[str]
    TaxLevelCode: str #Optional[str] # code
    ExemptionReasonCode: str #Optional[str] # code
    ExemptionReason: str #Optional[str]
    RegistrationAddress: RegistrationAddress #Optional[
    TaxScheme: TaxScheme
   
@dataclass 
class PartyName():
    Name: str 

@dataclass 
class PartyIdentification():
    ID: str 
    
@dataclass 
class PayeeParty():
    WebsiteURI: str #Optional[str]
    LogoReferenceID: str #Optional[str]
    EndpointID: str #Optional[str]
    PartyIdentification: PartyIdentification #Optional[ #multiple instances possible
    PartyName: PartyName #Optional[ #multiple instances possible
    #Language Optional[
    PostalAddress: PostalAddress #Optional[PostalAddress
    #PhysicalLocation Optional[
    PartyTaxScheme: PartyTaxScheme #Optional[ #multiple instances possible
    PartyLegalEntity: PartyLegalEntity
    Contact: Contact #Optional[Contact]
    #Person Optional[

@dataclass 
class Party():
    WebsiteURI: str #Optional[int]
    LogoReferenceID: str #Optional[int]
    EndpointID: str #optional for BuyerCustomerParty, and SellerSupplierParty
    PartyIdentification: PartyIdentification #Optional[ #multiple instances possible
    PartyName: PartyName #Optional[ #multiple instances possible
    #Language Optional[
    PostalAddress: PostalAddress #Optional[PostalAddress
    #PhysicalLocation Optional[
    PartyTaxScheme: PartyTaxScheme #Optional[ #multiple instances possible
    PartyLegalEntity: PartyLegalEntity
    Contact: Contact #(Optional for AccountingSupplierParty, BuyerCustomerParty, and SellerSupplierParty, but mandatory for AccountingCustomerParty)
    #Person Optional[


@dataclass 
class Delivery():
    ID: str #Optional[int]
    Quantity: float #Optional[float] #datatype: quantity
    MinimumQuantity: float #Optional[float] #datatype: quantity
    MaximumQuantity: float #Optional[float] #datatype: quantity
    ActualDeliveryDate: date #Optional[date]
    ActualDeliveryTime: time #Optional[time]
    LatestDeliveryDate: date #Optional[date]
    LatestDeliveryTime: time #Optional[time]
    TrackingID: str #Optional[str]
    #DeliveryLocation #Optional[
    #RequestedDeliveryPeriod #Optional[
    #DeliveryParty #Optional[
    #Despatch #Optional[

@dataclass 
class SellerSupplierParty():
    CustomerAssignedAccountID: str #Optional[int]
    AdditionalAccountID: str #Optional[List[int]] #multiple instances possible
    Party: Party
    #DespatchContact: Optional[
    #AccountingContact: Optional[
    #SellerContact: Optional[

@dataclass 
class BuyerCustomerParty():
    CustomerAssignedAccountID: str #Optional[int]
    SupplierAssignedAccountID: str #Optional[List[int]] #multiple instances possible
    AdditionalAccountID: str #Optional[List[int]] #multiple instances possible
    Party: Party
    #DeliveryContact: Optional[
    #AccountingContact: Optional[
    #BuyerContact: Optional[

@dataclass 
class AccountingCustomerParty():
    CustomerAssignedAccountID: str #Optional[int]
    SupplierAssignedAccountID: str #Optional[int]
    AdditionalAccountID: str #Optional[List[int]] #multiple instances possible
    Party: Party
    #DespatchContact: Optional[
    #AccountingContact: Optional[
    #SellerContact: Optional[

@dataclass 
class AccountingSupplierParty():
    CustomerAssignedAccountID: str #Optional[int]
    AdditionalAccountID: str #Optional[List[int]] #multiple instances possible
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
    UUID: str #Optional[int]
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
    ExchangeMarketID: str #Optional[int]
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
    ExtendedID: str #Optional[int]
    #IssuerParty #Optional[

@dataclass 
class SellersItemIdentification():
    ID: int
    ExtendedID: str #Optional[int]
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
    OriginAddress: OriginAddress #Optional[
    #ItemInstance #Optional[List[]] #multiple instances possible

@dataclass 
class OrderReference():
    ID: int
    SalesOrderID: str #Optional[int]
    CopyIndicator: bool #Optional[bool]
    UUID: str #Optional[int]
    IssueDate: date #Optional[date] #date type (yyyy-mm-dd)
    IssueTime: time #Optional[time] #time type (00:00:00)
    SalesOrderID: str #Optional[int]
    CustomerReference: str #Optional[str]
    DocumentReference: DocumentReference #Optional[DocumentReference]

@dataclass 
class OrderLineReference():
    LineID: int
    SalesOrderLineID: str #Optional[int]
    UUID: str #Optional[int]
    LineStatusCode: str #Optional[str] #datatype: code
    OrderReference: OrderReference #Optional[OrderReference]

@dataclass 
class InvoiceLine():
    ID: str 
    UUID: str #Optional[int]
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
    UBLVersionID: str # identifier
    CustomizationID: int
    ProfileID: int
    ID: int
    CopyIndicator: bool #Optional[bool]
    UUID: str #Optional[int]
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
    PaymentTerms: PaymentTerms #Optional[ - multiple instances possible
    # PrepaidPayment Optional[ - multiple instances possible
    AllowanceCharge: AllowanceCharge #Optional[ - multiple instances possible
    TaxExchangeRate: TaxExchangeRate #Optional[TaxExchangeRate]
    PricingExchangeRate: PricingExchangeRate #Optional[PricingExchangeRate]
    PaymentExchangeRate: PaymentExchangeRate #Optional[PaymentExchangeRate]
    PaymentAlternativeExchangeRate: PaymentAlternativeExchangeRate #Optional[PaymentAlternativeExchangeRate]
    TaxTotal: TaxTotal # - multiple instances possible
    LegalMonetaryTotal: LegalMonetaryTotal
    InvoiceLine: InvoiceLine # - multiple instances possible
