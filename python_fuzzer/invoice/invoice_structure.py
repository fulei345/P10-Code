from datetime import date, time
from typing import Optional, List, Union, Any
from dataclasses import dataclass, fields


@dataclass 
class Payment():
    ID: str #Optional[str]
    PaidAmount: float #Optional[float] #datatype: amount
    ReceivedDate: date #Optional[date] 
    PaidDate: date #Optional[date] 
    PaidTime: time #Optional[time]   
    InstructionID: str #Optional[str] 


@dataclass 
class Period():
    StartDate: date #Optional[date]
    StartTime: time #Optional[time]
    EndDate: date #Optional[date]
    EndTime: time #Optional[time]
    DurationMeasure: int #Optional[int] #measure Type
    DescriptionCode: str #Optional[str] # code #multiple instances possible
    Description: str #Optional[str] #multiple instances possible


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
class Country():
    IdentificationCode: str #Optional[str] # code
    Name: str #Optional[str]

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
class TaxScheme():
    ID: str #Optional[str]
    Name: str #Optional[str] # name
    TaxTypeCode: str #Optional[str] # code
    CurrencyCode: str #Optional[str] # code
    JurisdictionRegionAddress: Address #Optional[ #multiple instances possible


@dataclass 
class TaxCategory():
    ID: str #Optional[str]
    Name: str #Optional[str] #datatype: name
    Percent: str #Optional[str] #Percent Type
    BaseUnitMeasure: int #Optional[int] #measure Type
    PerUnitAmount: float #Optional[float] #datatype: amoun
    TaxExemptionReasonCode: str #Optional[str] #datatype: code
    TaxExemptionReason: str #Optional[str] 
    TierRange: str #Optional[str] 
    TierRatePercent: str #Optional[str] #Percent Type
    TaxScheme: TaxScheme
    
@dataclass 
class TaxSubtotal(): #!
    TaxableAmount: float #Optional[float] #datatype: amount
    TaxAmount: float #datatype: amount
    CalculationSequenceNumeric: int #Optional[int] #numeric
    TransactionCurrencyTaxAmount: float #Optional[float] #datatype: amount
    Percent: str #Optional[str] #Percent Type
    BaseUnitMeasure: int #Optional[int] #measure Type
    PerUnitAmount: float #Optional[float] #datatype: amount
    TierRange: str #Optional[str] 
    TierRatePercent: str #Optional[str] #Percent Type  
    TaxCategory: TaxCategory
      
@dataclass 
class TaxTotal(): #!
    TaxAmount: float #datatype: amount
    RoundingAmount: float #Optional[float] #datatype: amount
    TaxEvidenceIndicator: bool #Optional[bool] 
    TaxIncludedIndicator: bool #Optional[bool] 
    TaxSubtotal: TaxSubtotal #Optional[] #multiple instances possible

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
    SettlementPeriod: Period #Optional[Period
    PenaltyPeriod: Period #Optional[Period
    #TradeFinancing #Optional[TradeFinancing

@dataclass 
class FinancialInstitutionBranch():
    ID: str #Optional[str]
    Name: str #Optional[str] #datatype: name
    #FinancialInstitution #Optional[
    Address: Address #Optional[

@dataclass 
class FinancialAccount():
    ID: str #Optional[str]
    Name: str #Optional[str] #datatype: name
    AliasName: str #Optional[str] #datatype: name
    AccountTypeCode: str #Optional[str] #datatype: code
    AccountFormatCode: str #Optional[str] #datatype: code
    CurrencyCode: str #Optional[str] #datatype: code
    PaymentNote: str #Optional[str] #multiple instances possible
    #FinancialInstitutionBranch #Optional[
    Country: Country #Optional[Country
    
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
    PayerFinancialAccount: FinancialAccount #Optional[ 
    PayeeFinancialAccount: FinancialAccount #Optional[ 
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
    TaxCategory: TaxCategory #Optional[] #multiple instances possible
    TaxTotal: TaxTotal #Optional[] 
    PaymentMeans: PaymentMeans #Optional[] #multiple instances possible

@dataclass 
class DeliveryLocation():
    ID: str 
    Description: str #Optional[str] 
    Conditions: str #Optional[str] 
    CountrySubentity: str #Optional[str] 
    CountrySubentityCode: str #Optional[str] # code
    ValidityPeriod: Period #Optional[Period
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
    ID: str
    Name: str #Optional[str] #datatype: name
    Telephone: str #Optional[str]
    Telefax: str #Optional[str]
    ElectronicMail: str #Optional[str]
    Note: str #Optional[str]
    OtherCommunication: OtherCommunication #Optional[OtherCommunication]


@dataclass 
class Attachment():
    EmbeddedDocumentBinaryObject: bytes #Optional[bytes] # binary type
    #ExternalReference Optional[

@dataclass 
class DocumentReference():
    ID: str
    CopyIndicator: bool #Optional[bool]
    UUID: str #Optional[int]
    IssueDate: date #Optional[date] #date type (yyyy-mm-dd)
    XPath: str #Optional[List[str]] #multiple instances possible
    Attachment: Attachment #Optional[Attachment]

@dataclass 
class PartyLegalEntity(): #!
    RegistrationName: str #Optional[str] # name
    CompanyID: str #Optional[int]
    CompanyTypeCode: str #Optional[str] # code
    CompanyLiquidationStatusCode: str #Optional[str] # code
    RegistrationDate: date #Optional[date]
    RegistrationExpirationDate: date #Optional[date]
    CorporateStockAmount: float #Optional[float] #datatype: amount
    RegistrationAddress: Address #Optional[
    #CorporateRegistrationScheme Optional[
    #StakeholderParty: 'Party' #Optional[Party #multiple instances possible #TODO test this one plz and op
    CompanyDossierDocumentReference: DocumentReference #Optional[DocumentReference


@dataclass 
class PartyTaxScheme():
    RegistrationName: str #Optional[str] # name
    CompanyID: str #Optional[str]
    TaxLevelCode: str #Optional[str] # code
    ExemptionReasonCode: str #Optional[str] # code
    ExemptionReason: str #Optional[str]
    RegistrationAddress: Address #Optional[
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
    PostalAddress: Address #Optional[Address
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
    PostalAddress: Address #Optional[Address
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
    RequestedDeliveryPeriod: Period #Optional[Period
    DeliveryParty: Party #Optional[Party
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
class Signature():
    ID: str 
    Note: str #Optional[str]
    ValidationDate: date #Optional[date]
    ValidationTime: time #Optional[time]
    ValidatorID: str #Optional[str]
    CanonicalizationMethod: str #Optional[str]
    SignatureMethod: str #Optional[str]
    SignatoryParty: Party
    DigitalSignatureAttachment: Attachment #Optional[Attachment]
    OriginalDocumentReference: DocumentReference #Optional[DocumentReference]
    
@dataclass 
class ForeignExchangeContract():
    ID: str
    IssueDate: date #Optional[date] 
    IssueTime: time #Optional[time]
    ContractTypeCode: str #Optional[str] # code
    ContractType: str #Optional[str]
    ValidityPeriod: Period #Optional[Period
    ContractDocumentReference: DocumentReference #Optional[DocumentReference]

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
    InvoiceDocumentReference: DocumentReference #Optional[InvoiceDocumentReference]
    SelfBilledInvoiceDocumentReference: DocumentReference #Optional[SelfBilledInvoiceDocumentReference]
    CreditNoteDocumentReference: DocumentReference #Optional[CreditNoteDocumentReference]
    SelfBilledCreditNoteDocumentReference: DocumentReference #Optional[SelfBilledCreditNoteDocumentReference]
    ReminderDocumentReference: DocumentReference #Optional[ReminderDocumentReference]

@dataclass 
class BuyersItemIdentification():
    ID: str
    ExtendedID: str #Optional[int]
    IssuerParty: Party #Optional[

@dataclass 
class SellersItemIdentification():
    ID: str
    ExtendedID: str #Optional[int]
    #PhysicalAttribute #Optional[List[]] #multiple instances possible
    #MeasurementDimension #Optional[List[]] #multiple instances possible
    IssuerParty: Party #Optional[

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
class Price(): #!
    PriceAmount: float #datatype: amount
    BaseQuantity: float #Optional[float] #datatype: quantity 
    PriceChangeReason: str #Optional[str] #multiple instances possible
    PriceTypeCode: str #Optional[str] # code
    PriceType: str #Optional[str] 
    OrderableUnitFactorRate: int #Optional[int] #rate
    ValidityPeriod: Period #Optional[Period #multiple instances possible
    # PriceList #Optional[ 
    AllowanceCharge: AllowanceCharge #Optional[ #multiple instances possible
    PricingExchangeRate: PricingExchangeRate

@dataclass 
class PricingReference():
    #OriginalItemLocationQuantity: ItemLocationQuantity #Optional[
    AlternativeConditionPrice: Price #Optional[Price] #multiple instances possible

@dataclass 
class Temperature():
    AttributeID: str 
    Measure: int #measure Type   
    Description: str #Optional[str] #multiple instances possible

@dataclass 
class HazardousGoodsTransit():
    TransportEmergencyCardCode: str #Optional[str] # code
    PackingCriteriaCode: str #Optional[str] # code
    HazardousRegulationCode: str #Optional[str] # code
    InhalationToxicityZoneCode: str #Optional[str] # code
    TransportAuthorizationCode: str #Optional[str] # code
    MaximumTemperature: Temperature #Optional[
    MinimumTemperature: Temperature #Optional[

@dataclass 
class SecondaryHazard():
    ID: str #Optional[str]
    PlacardNotation: str #Optional[str]     
    PlacardEndorsement: str #Optional[str] 
    EmergencyProceduresCode: str #Optional[str] # code
    Extension: str #Optional[str]

@dataclass 
class CommodityClassification():
    NatureCode: str #Optional[str] # code
    CargoTypeCode: str #Optional[str] # code
    CommodityCode: str #Optional[str] # code
    ItemClassificationCode: str #Optional[str] # code

@dataclass 
class TransactionConditions():
    ID: str #Optional[str]
    ActionCode: str #Optional[str] # code
    Description: str #Optional[str] #multiple instances possible
    DocumentReference: DocumentReference #Optional[DocumentReference] #multiple instances possible


@dataclass 
class ItemProperty():
    Name: str #Optional[str] # name
    NameCode: str #Optional[str] # code
    Value: str #Optional[str] #multiple instances possible
    ValueQuantity: float #Optional[float] #datatype: quantity
    Value: str #Optional[str] #multiple instances possible
    ImportanceCode: str #Optional[str] # code
    UsabilityPeriod: Period #Optional[Period
    #ItemPropertyGroup #Optional[List[]] #multiple instances possible
    #RangeDimension #Optional[

@dataclass 
class HazardousItem():
    ID: str #Optional[str]
    PlacardNotation: str #Optional[str] 
    PlacardEndorsement: str #Optional[str] 
    AdditionalInformation: str #Optional[str] 
    UNDGCode: str #Optional[str] # code
    EmergencyProceduresCode: str #Optional[str] # code
    MedicalFirstAidGuideCode: str #Optional[str] # code
    TechnicalName: str #Optional[str] # name
    CategoryName: str #Optional[str] # name
    HazardousCategoryCode: str #Optional[str] # code
    UpperOrangeHazardPlacardID: str #Optional[str]
    LowerOrangeHazardPlacardID: str #Optional[str]
    MarkingID: str #Optional[str]
    HazardClassID: str #Optional[str]
    NetWeightMeasure: int #Optional[int] #measure Type
    NetVolumeMeasure: int #Optional[int] #measure Type
    Quantity: float #Optional[float] #datatype: quantity
    ContactParty: Party #Optional[Party
    SecondaryHazard: SecondaryHazard #Optional[List[]] #multiple instances possible
    HazardousGoodsTransit: HazardousGoodsTransit #Optional[List[]] #multiple instances possible
    EmergencyTemperature: Temperature #Optional[
    FlashpointTemperature: Temperature #Optional[
    AdditionalTemperature: Temperature #Optional[List[]] #multiple instances possible

@dataclass 
class LotIdentification():
    LotNumberID: str #Optional[str]
    ExpiryDate: date #Optional[date] 
    AdditionalItemProperty: ItemProperty #Optional[List[]] #multiple instances possible

@dataclass 
class ItemInstance():
    ProductTraceID: str #Optional[str]
    ManufactureDate: date #Optional[date] 
    ManufactureTime: time #Optional[time]   
    BestBeforeDate: date #Optional[date] 
    RegistrationID: str #Optional[str] 
    SerialID: str #Optional[str] 
    AdditionalItemProperty: ItemProperty #Optional[List[]] #multiple instances possible
    LotIdentification: LotIdentification #Optional[

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
    CatalogueDocumentReference: DocumentReference #Optional[DocumentReference]
    ItemSpecificationDocumentReference: DocumentReference #Optional[DocumentReference]
    OriginCountry: Country #Optional[
    CommodityClassification: CommodityClassification #Optional[List[]] #multiple instances possible
    TransactionConditions: TransactionConditions #Optional[List[]] #multiple instances possible
    HazardousItem: HazardousItem #Optional[List[]] #multiple instances possible
    ClassifiedTaxCategory: TaxCategory #Optional[List[]] #multiple instances possible
    AdditionalItemProperty: ItemProperty #Optional[List[]] #multiple instances possible
    ManufacturerParty: Party #Optional[List[]] #multiple instances possible
    InformationContentProviderParty: Party #Optional[
    OriginAddress: Address #Optional[
    ItemInstance: ItemInstance #Optional[List[]] #multiple instances possible

@dataclass 
class OrderReference():
    ID: str
    SalesOrderID: str #Optional[int]
    CopyIndicator: bool #Optional[bool]
    UUID: str #Optional[int]
    IssueDate: date #Optional[date] #date type (yyyy-mm-dd)
    IssueTime: time #Optional[time] #time type (00:00:00)
    SalesOrderID: str #Optional[int]
    CustomerReference: str #Optional[str]
    DocumentReference: DocumentReference #Optional[DocumentReference]

@dataclass 
class LineReference():
    LineID: str
    UUID: str #Optional[int]
    LineStatusCode: str #Optional[str] #datatype: code
    DocumentReference: DocumentReference #Optional[DocumentReference]

@dataclass 
class OrderLineReference():
    LineID: str
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
    DespatchLineReference: LineReference #Optional[ #multiple instances possible
    ReceiptLineReference: LineReference #Optional[ #multiple instances possible
    BillingReference: BillingReference #Optional[List[BillingReference]] #multiple instances possible
    PricingReference: PricingReference #Optional[PricingReference 
    DocumentReference: DocumentReference #Optional[List[DocumentReference]] #multiple instances possible
    OriginatorParty: Party #Optional[ 
    Delivery: Delivery #Optional[List[Delivery]] #multiple instances possible
    AllowanceCharge: AllowanceCharge #Optional[ #multiple instances possible
    TaxTotal: TaxTotal #multiple instances possible
    Item: Item 
    Price: Price

@dataclass 
class UBLExtension(): #?????????????????????????????`?????????????```?`?????`
    ID: str #Optional[str]
    Name: str #Optional[str] #datatype: name
    ExtensionAgencyID: str #Optional[str]
    ExtensionAgencyName: str #Optional[str] #datatype: name
    ExtensionVersionID: str #Optional[str]
    ExtensionAgencyURI: str #Optional[str]
    ExtensionURI: str #Optional[str]
    ExtensionReasonCode: str #Optional[str] #code
    ExtensionReason: str #Optional[str]
    ExtensionContent: str 

@dataclass 
class UBLExtensions():
    UBLExtension: UBLExtension #multiple instances possible

@dataclass #provide automatic generation of __init__(), among other things
class Invoice():
    UBLExtensions: UBLExtensions #Optional[
    UBLVersionID: str # identifier
    CustomizationID: str
    ProfileID: str
    ID: str
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
    InvoicePeriod: Period #Optional[Period
    OrderReference: OrderReference #Optional[OrderReference]
    BillingReference: BillingReference #Optional[List[BillingReference]] # multiple instances possible
    DespatchDocumentReference: DocumentReference #Optional[List[DespatchDocumentReference]] # multiple instances possible
    ReceiptDocumentReference: DocumentReference #Optional[List[ReceiptDocumentReference]] # multiple instances possible
    OriginatorDocumentReference: DocumentReference #Optional[List[OriginatorDocumentReference]] # multiple instances possible
    ContractDocumentReference: DocumentReference #Optional[ContractDocumentReference]
    AdditionalDocumentReference: DocumentReference #Optional[ - multiple instances possible
    Signature: Signature #Optional[ - multiple instances possible
    AccountingSupplierParty: AccountingSupplierParty
    AccountingCustomerParty: AccountingCustomerParty
    PayeeParty: PayeeParty #Optional[PayeeParty]
    BuyerCustomerParty: BuyerCustomerParty #Optional[BuyerCustomerParty]
    SellerSupplierParty: SellerSupplierParty #Optional[SellerSupplierParty]
    Delivery: Delivery #Optional[ - multiple instances possible
    DeliveryTerms: DeliveryTerms #Optional[
    PaymentMeans: PaymentMeans #Optional[ - multiple instances possible
    PaymentTerms: PaymentTerms #Optional[ - multiple instances possible
    PrepaidPayment: Payment #Optional[ - multiple instances possible
    AllowanceCharge: AllowanceCharge #Optional[ - multiple instances possible
    TaxExchangeRate: TaxExchangeRate #Optional[TaxExchangeRate]
    PricingExchangeRate: PricingExchangeRate #Optional[PricingExchangeRate]
    PaymentExchangeRate: PaymentExchangeRate #Optional[PaymentExchangeRate]
    PaymentAlternativeExchangeRate: PaymentAlternativeExchangeRate #Optional[PaymentAlternativeExchangeRate]
    TaxTotal: TaxTotal # - multiple instances possible
    LegalMonetaryTotal: LegalMonetaryTotal
    InvoiceLine: InvoiceLine # - multiple instances possible


invoice_type_dict={'LegalMonetaryTotal': LegalMonetaryTotal,
'Country': Country,
'Address': Address,
'JurisdictionRegionAddress': Address,
'RegistrationAddress': Address,
'PostalAddress': Address,
'OriginAddress': Address,
'TaxScheme': TaxScheme,
'TaxCategory': TaxCategory,
'ClassifiedTaxCategory': TaxCategory,
'TaxSubtotal': TaxSubtotal,
'TaxTotal': TaxTotal,
'PaymentTerms': PaymentTerms,
'FinancialInstitutionBranch': FinancialInstitutionBranch,
'FinancialAccount': FinancialAccount,
'PayerFinancialAccount': FinancialAccount,
'PayeeFinancialAccount': FinancialAccount,
'PaymentMeans': PaymentMeans,
'AllowanceCharge': AllowanceCharge,
'DeliveryLocation': DeliveryLocation,
'DeliveryTerms': DeliveryTerms,
'OtherCommunication': OtherCommunication,
'Contact': Contact,
'PartyLegalEntity': PartyLegalEntity,
'PartyTaxScheme': PartyTaxScheme,
'PartyName': PartyName,
'PartyIdentification': PartyIdentification,
'PayeeParty': PayeeParty,
'Party': Party,
'Delivery': Delivery,
'SellerSupplierParty': SellerSupplierParty,
'BuyerCustomerParty': BuyerCustomerParty,
'AccountingCustomerParty': AccountingCustomerParty,
'AccountingSupplierParty': AccountingSupplierParty,
'Attachment': Attachment,
'DocumentReference': DocumentReference,
'ContractDocumentReference': DocumentReference,
'AdditionalDocumentReference': DocumentReference,
'InvoiceDocumentReference': DocumentReference,
'SelfBilledInvoiceDocumentReference': DocumentReference,
'CreditNoteDocumentReference': DocumentReference,
'SelfBilledCreditNoteDocumentReference': DocumentReference,
'ReminderDocumentReference': DocumentReference,
'CatalogueDocumentReference': DocumentReference,
'DespatchDocumentReference': DocumentReference,
'ReceiptDocumentReference': DocumentReference,
'OriginatorDocumentReference': DocumentReference,
'ForeignExchangeContract': ForeignExchangeContract,
'TaxExchangeRate': TaxExchangeRate,
'PaymentAlternativeExchangeRate': PaymentAlternativeExchangeRate,
'PaymentExchangeRate': PaymentExchangeRate,
'PricingExchangeRate': PricingExchangeRate,
'BillingReference': BillingReference,
'BuyersItemIdentification': BuyersItemIdentification,
'SellersItemIdentification': SellersItemIdentification,
'ManufacturersItemIdentification': ManufacturersItemIdentification,
'StandardItemIdentification': StandardItemIdentification,
'CatalogueItemIdentification': CatalogueItemIdentification,
'AdditionalItemIdentification': AdditionalItemIdentification,
'Price': Price,
'Item': Item,
'OrderReference': OrderReference,
'OrderLineReference': OrderLineReference,
'InvoiceLine': InvoiceLine,
'Invoice': Invoice,
'Signature': Signature,
'SignatoryParty': Party,
'DigitalSignatureAttachment': Attachment,
'OriginalDocumentReference': DocumentReference,
'InvoicePeriod': Period,
'SettlementPeriod': Period,
'PenaltyPeriod': Period,
'ValidityPeriod': Period,
'RequestedDeliveryPeriod': Period,
'CompanyDossierDocumentReference': DocumentReference,
'ItemSpecificationDocumentReference': DocumentReference,
'StakeholderParty': Party,
'DeliveryParty': Party,
'IssuerParty': Party,
'ManufacturerParty': Party,
'InformationContentProviderParty': Party,
'OriginatorParty': Party,
'PrepaidPayment': Payment,
'UBLExtensions': UBLExtensions,
'UBLExtension': UBLExtension,
'PricingReference': PricingReference,
'DespatchLineReference': LineReference,
'ReceiptLineReference': LineReference,
'OriginCountry': Country,
'ItemInstance': ItemInstance,
'AdditionalItemProperty': ItemProperty,
'HazardousItem': HazardousItem,
'TransactionConditions': TransactionConditions,
'CommodityClassification': CommodityClassification,
'LotIdentification': LotIdentification,
'SecondaryHazard': SecondaryHazard,
'HazardousGoodsTransit': HazardousGoodsTransit,
'EmergencyTemperature': Temperature,
'FlashpointTemperature': Temperature,
'AdditionalTemperature': Temperature,
'MaximumTemperature': Temperature,
'MinimumTemperature': Temperature
}
