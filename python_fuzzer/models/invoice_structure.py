from datetime import date, time
from typing import Optional, List, Union, Any, TYPE_CHECKING
from dataclasses import dataclass, fields


@dataclass 
class Payment():
    ID: Optional[str]
    PaidAmount: Optional[float] #datatype: amount
    ReceivedDate: Optional[date] 
    PaidDate: Optional[date] 
    PaidTime: Optional[time]   
    InstructionID: Optional[str] 


@dataclass 
class Period():
    StartDate: Optional[date]
    StartTime: Optional[time]
    EndDate: Optional[date]
    EndTime: Optional[time]
    DurationMeasure: Optional[float] #measure Type
    DescriptionCode: Optional[List[str]] # code #multiple instances possible
    Description: Optional[List[str]] #multiple instances possible

@dataclass 
class LegalMonetaryTotal(): #!
    LineExtensionAmount: Optional[float] #datatype: amount
    TaxExclusiveAmount: Optional[float] #datatype: amount
    TaxInclusiveAmount: Optional[float] #datatype: amount
    AllowanceTotalAmount: Optional[float] #datatype: amount
    ChargeTotalAmount: Optional[float] #datatype: amount
    PrepaidAmount: Optional[float] #datatype: amount
    PayableRoundingAmount: Optional[float] #datatype: amount
    PayableAmount: float #datatype: amount
    PayableAlternativeAmount: Optional[float] #datatype: amount

@dataclass 
class Country():
    IdentificationCode: Optional[str] # code
    Name: Optional[str]

@dataclass 
class Temperature():
    AttributeID: str 
    Measure: float #measure Type   
    Description: Optional[List[str]] #multiple instances possible

@dataclass 
class LocationCoordinate():
    CoordinateSystemCode: Optional[str] # code
    LatitudeDegreesMeasure: Optional[float] #measure Type
    LatitudeMinutesMeasure: Optional[float] #measure Type
    LatitudeDirectionCode: Optional[str] # code
    LongitudeDegreesMeasure: Optional[float] #measure Type
    LongitudeMinutesMeasure: Optional[float] #measure Type
    LongitudeDirectionCode: Optional[str] # code
    
@dataclass 
class AddressLine():
    Line: str

@dataclass 
class Address():
    ID: Optional[str]
    AddressTypeCode: Optional[str] # code
    AddressFormatCode: Optional[str] # code
    Postbox: Optional[str] 
    Floor: Optional[str]
    Room: Optional[str]
    StreetName: Optional[str] # name
    AdditionalStreetName: Optional[str] # name
    BlockName: Optional[str] # name
    BuildingName: Optional[str] # name
    BuildingNumber: Optional[str]
    InhouseMail: Optional[str]
    Department: Optional[str]
    MarkAttention: Optional[str]
    MarkCare: Optional[str]
    PlotIdentification: Optional[str]
    CitySubdivisionName: Optional[str] # name
    CityName: Optional[str] # name
    PostalZone: Optional[str]
    CountrySubentity: Optional[str]
    CountrySubentityCode: Optional[str] # code
    Region: Optional[str] 
    District: Optional[str]
    TimezoneOffset: Optional[str]
    AddressLine: Optional[List[AddressLine]] #multiple instances possible
    Country: Optional[Country]
    LocationCoordinate: Optional[LocationCoordinate]

@dataclass 
class TaxScheme():
    ID: Optional[str]
    Name: Optional[str] # name
    TaxTypeCode: Optional[str] # code
    CurrencyCode: Optional[str] # code
    JurisdictionRegionAddress: Optional[List[Address]] #multiple instances possible

@dataclass 
class TaxCategory():
    ID: Optional[str]
    Name: Optional[str] #datatype: name
    Percent: Optional[str] #Percent Type
    BaseUnitMeasure: Optional[float] #measure Type
    PerUnitAmount: Optional[float] #datatype: amoun
    TaxExemptionReasonCode: Optional[str] #datatype: code
    TaxExemptionReason: Optional[str] 
    TierRange: Optional[str] 
    TierRatePercent: Optional[str] #Percent Type
    TaxScheme: TaxScheme
    
@dataclass 
class TaxSubtotal(): #!
    TaxableAmount: Optional[float] #datatype: amount
    TaxAmount: float #datatype: amount
    CalculationSequenceNumeric: Optional[float] #numeric
    TransactionCurrencyTaxAmount: Optional[float] #datatype: amount
    Percent: Optional[str] #Percent Type
    BaseUnitMeasure: Optional[float] #measure Type
    PerUnitAmount: Optional[float] #datatype: amount
    TierRange: Optional[str] 
    TierRatePercent: Optional[str] #Percent Type  
    TaxCategory: TaxCategory
      
@dataclass 
class TaxTotal(): #!
    TaxAmount: float #datatype: amount
    RoundingAmount: Optional[float] #datatype: amount
    TaxEvidenceIndicator: Optional[bool] 
    TaxIncludedIndicator: Optional[bool] 
    TaxSubtotal: Optional[List[TaxSubtotal]] #multiple instances possible

@dataclass 
class FinancialInstitution():
    ID: Optional[str]
    Name: Optional[str] #datatype: name
    Address: Optional[Address]

@dataclass 
class FinancialInstitutionBranch():
    ID: Optional[str]
    Name: Optional[str] #datatype: name
    FinancialInstitution: Optional[FinancialInstitution]
    Address: Optional[Address]

@dataclass 
class FinancialAccount():
    ID: Optional[str]
    Name: Optional[str] #datatype: name
    AliasName: Optional[str] #datatype: name
    AccountTypeCode: Optional[str] #datatype: code
    AccountFormatCode: Optional[str] #datatype: code
    CurrencyCode: Optional[str] #datatype: code
    PaymentNote: Optional[List[str]] #multiple instances possible
    FinancialInstitutionBranch: Optional[FinancialInstitutionBranch]
    Country: Optional[Country]

@dataclass 
class CardAccount():
    PrimaryAccountNumberID: str
    NetworkID: str
    CardTypeCode: Optional[str] #code
    ValidityStartDate: Optional[date] 
    ExpiryDate: Optional[date] 
    IssuerID: Optional[str]
    IssueNumberID: Optional[str]
    CV2ID: Optional[str]
    CardChipCode: Optional[str] #code
    ChipApplicationID: Optional[str]
    HolderName: Optional[str] #datatype: name

@dataclass 
class CreditAccount():
    AccountID: str

@dataclass 
class PaymentMeans():
    ID: Optional[str]
    PaymentMeansCode: str #datatype: code
    PaymentDueDate: Optional[date]
    PaymentChannelCode: Optional[str] #datatype: code
    InstructionID: Optional[str]
    InstructionNote: Optional[str] 
    PaymentID: Optional[List[str]] #multiple instances possible
    CardAccount: Optional[CardAccount] 
    PayerFinancialAccount: Optional[FinancialAccount] 
    PayeeFinancialAccount: Optional[FinancialAccount]
    CreditAccount: Optional[CreditAccount] 
    
@dataclass 
class AllowanceCharge(): #!
    ID: Optional[str]
    ChargeIndicator: bool 
    AllowanceChargeReasonCode: Optional[str] #datatype: code
    AllowanceChargeReason: Optional[str]
    MultiplierFactorNumeric: Optional[float] #numeric
    PrepaidIndicator: Optional[bool]
    SequenceNumeric: Optional[float] #numeric
    Amount: float #datatype: amount
    BaseAmount: Optional[float] #datatype: amount
    AccountingCostCode: Optional[str] #datatype: code
    AccountingCost: Optional[str] 
    TaxCategory: Optional[List[TaxCategory]] #multiple instances possible
    TaxTotal: Optional[TaxTotal] 
    PaymentMeans: Optional[List[PaymentMeans]] #multiple instances possible

@dataclass 
class Location():
    ID: str 
    Description: Optional[str] 
    Conditions: Optional[str] 
    CountrySubentity: Optional[str] 
    CountrySubentityCode: Optional[str] # code
    ValidityPeriod: Optional[Period]
    Address: Optional[Address]

@dataclass 
class DeliveryTerms():
    ID: Optional[str]  
    SpecialTerms: Optional[str] 
    LossRiskResponsibilityCode: Optional[str] # code
    LossRisk: Optional[str]  
    DeliveryLocation: Optional[Location]

@dataclass 
class OtherCommunication(): #!
    ChannelCode: Optional[str] #datatype code 
    Channel: Optional[str] #datatype text
    Value: str #datatype text

@dataclass 
class Contact():
    ID: str
    Name: Optional[str] #datatype: name
    Telephone: Optional[str]
    Telefax: Optional[str]
    ElectronicMail: Optional[str]
    Note: Optional[str]
    OtherCommunication: Optional[OtherCommunication]

@dataclass 
class ExternalReference():
    URI: Optional[str]
    DocumentHash: Optional[str]
    ExpiryDate: Optional[date] 
    ExpiryTime: Optional[time] 
    MimeCode: Optional[str] # code
    FormatCode: Optional[str] # code
    EncodingCode: Optional[str] # code
    CharacterSetCode: Optional[str] # code
    FileName: Optional[str] # name
    
@dataclass 
class Attachment():
    EmbeddedDocumentBinaryObject: Optional[bytes] # binary type
    ExternalReference: Optional[ExternalReference]

@dataclass 
class DocumentReference():
    ID: str
    CopyIndicator: Optional[bool]
    UUID: Optional[str]
    IssueDate: Optional[date] #date type (yyyy-mm-dd)
    XPath: Optional[List[str]] #multiple instances possible
    Attachment: Optional[Attachment]

@dataclass 
class CorporateRegistrationScheme():
    ID: Optional[str]
    Name: Optional[str] # name
    CorporateRegistrationTypeCode: Optional[str] # code
    JurisdictionRegionAddress: Optional[List[Address]] #multiple instances possible

@dataclass 
class PartyLegalEntity(): #!
    RegistrationName: Optional[str] # name
    CompanyID: Optional[str]
    CompanyTypeCode: Optional[str] # code
    CompanyLiquidationStatusCode: Optional[str] # code
    RegistrationDate: Optional[date]
    RegistrationExpirationDate: Optional[date]
    CorporateStockAmount: Optional[float] #datatype: amount
    RegistrationAddress: Optional[Address]
    CorporateRegistrationScheme: Optional[CorporateRegistrationScheme]
    StakeholderParty: Optional['Party'] #multiple instances possible
    CompanyDossierDocumentReference: Optional[DocumentReference]

@dataclass 
class PartyTaxScheme():
    RegistrationName: Optional[str] # name
    CompanyID: Optional[str]
    TaxLevelCode: Optional[str] # code
    ExemptionReasonCode: Optional[str] # code
    ExemptionReason: Optional[str]
    RegistrationAddress: Optional[Address]
    TaxScheme: TaxScheme
   
@dataclass 
class PartyName():
    Name: str 

@dataclass 
class PartyIdentification():
    ID: str 
    
@dataclass 
class Language():
    ID: Optional[str]
    Name: Optional[str] # name
    LocaleCode: Optional[str] # code

@dataclass 
class Person():
    FirstName: Optional[str] # name
    FamilyName: Optional[str] # name
    Title: Optional[str] 
    MiddleName: Optional[str] # name
    NameSuffix: Optional[str] 
    JobTitle: Optional[str] 
    OrganizationDepartment: Optional[str] 
    Contact: Optional[Contact]
    
@dataclass 
class PayeeParty():
    WebsiteURI: Optional[str]
    LogoReferenceID: Optional[str]
    EndpointID: Optional[str]
    PartyIdentification: Optional[List[PartyIdentification]] #multiple instances possible
    PartyName: Optional[List[PartyName]] #multiple instances possible
    Language: Optional[Language]
    PostalAddress: Optional[Address]
    PhysicalLocation: Optional[Location]
    PartyTaxScheme: Optional[List[PartyTaxScheme]] #multiple instances possible
    PartyLegalEntity: PartyLegalEntity
    Contact: Optional[Contact]
    Person: Optional[Person]

@dataclass 
class Party():
    WebsiteURI: Optional[str]
    LogoReferenceID: Optional[str]
    EndpointID: str #optional for BuyerCustomerParty, and SellerSupplierParty
    PartyIdentification: Optional[List[PartyIdentification]] #multiple instances possible
    PartyName: Optional[List[PartyName]] #multiple instances possible
    Language: Optional[Language]
    PostalAddress: Optional[Address]
    PhysicalLocation: Optional[Location]
    PartyTaxScheme: Optional[List[PartyTaxScheme]] #multiple instances possible
    PartyLegalEntity: PartyLegalEntity
    Contact: Contact #(Optional for AccountingSupplierParty, BuyerCustomerParty, and SellerSupplierParty, but mandatory for AccountingCustomerParty)
    Person: Optional[Person]

@dataclass 
class Despatch():
    ID: Optional[str]
    RequestedDespatchDate: Optional[date]
    RequestedDespatchTime: Optional[time]
    EstimatedDespatchDate: Optional[date]
    EstimatedDespatchTime: Optional[time]
    ActualDespatchDate: Optional[date]
    ActualDespatchTime: Optional[time]
    DespatchAddress: Optional[Address]
    DespatchParty: Optional[Party]
    Contact: Optional[Contact]
        
@dataclass 
class Delivery():
    ID: Optional[str]
    Quantity: Optional[float] #datatype: quantity
    MinimumQuantity: Optional[float] #datatype: quantity
    MaximumQuantity: Optional[float] #datatype: quantity
    ActualDeliveryDate: Optional[date]
    ActualDeliveryTime: Optional[time]
    LatestDeliveryDate: Optional[date]
    LatestDeliveryTime: Optional[time]
    TrackingID: Optional[str]
    DeliveryLocation: Optional[Location]
    RequestedDeliveryPeriod: Optional[Period]
    DeliveryParty: Optional[Party]
    Despatch: Optional[Despatch]

@dataclass 
class SellerSupplierParty():
    CustomerAssignedAccountID: Optional[str]
    AdditionalAccountID: Optional[List[str]] #multiple instances possible
    Party: Party
    DespatchContact: Optional[Contact]
    AccountingContact: Optional[Contact]
    SellerContact: Optional[Contact]

@dataclass 
class BuyerCustomerParty():
    CustomerAssignedAccountID: Optional[str]
    SupplierAssignedAccountID: Optional[List[str]] #multiple instances possible
    AdditionalAccountID: Optional[List[str]] #multiple instances possible
    Party: Party
    DeliveryContact: Optional[Contact]
    AccountingContact: Optional[Contact]
    BuyerContact: Optional[Contact]

@dataclass 
class AccountingCustomerParty():
    CustomerAssignedAccountID: Optional[str]
    SupplierAssignedAccountID: Optional[str]
    AdditionalAccountID: Optional[List[str]] #multiple instances possible
    Party: Party
    DespatchContact: Optional[Contact]
    AccountingContact: Optional[Contact]
    SellerContact: Optional[Contact]

@dataclass 
class AccountingSupplierParty():
    CustomerAssignedAccountID: Optional[str]
    AdditionalAccountID: Optional[List[str]] #multiple instances possible
    Party: Party
    DeliveryContact: Optional[Contact]
    AccountingContact: Optional[Contact]
    BuyerContact: Optional[Contact]


@dataclass 
class Signature():
    ID: str 
    Note: Optional[str]
    ValidationDate: Optional[date]
    ValidationTime: Optional[time]
    ValidatorID: Optional[str]
    CanonicalizationMethod: Optional[str]
    SignatureMethod: Optional[str]
    SignatoryParty: Party
    DigitalSignatureAttachment: Optional[Attachment]
    OriginalDocumentReference: Optional[DocumentReference]
    
@dataclass 
class ForeignExchangeContract():
    ID: str
    IssueDate: Optional[date] 
    IssueTime: Optional[time]
    ContractTypeCode: Optional[str] # code
    ContractType: Optional[str]
    ValidityPeriod: Optional[Period]
    ContractDocumentReference: Optional[DocumentReference]

@dataclass 
class TaxExchangeRate():
    SourceCurrencyCode: str # code 
    SourceCurrencyBaseRate: Optional[float] #rate
    TargetCurrencyCode: str # code
    TargetCurrencyBaseRate: Optional[float] #rate
    ExchangeMarketID: Optional[str]
    CalculationRate: Optional[float] #rate
    MathematicOperatorCode: Optional[str] # code
    Date: Optional[date]
    ForeignExchangeContract: Optional[ForeignExchangeContract]

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
    InvoiceDocumentReference: Optional[DocumentReference]
    SelfBilledInvoiceDocumentReference: Optional[DocumentReference]
    CreditNoteDocumentReference: Optional[DocumentReference]
    SelfBilledCreditNoteDocumentReference: Optional[DocumentReference]
    ReminderDocumentReference: Optional[DocumentReference]

@dataclass 
class Dimension():
    AttributeID: str
    Measure: Optional[float] #measure Type
    Description: Optional[List[str]] #multiple instances possible
    MinimumMeasure: Optional[float] #measure Type - actually float
    MaximumMeasure: Optional[float] #measure Type
    
@dataclass 
class BuyersItemIdentification():
    ID: str
    ExtendedID: Optional[str]
    IssuerParty: Optional[Party]

@dataclass 
class PhysicalAttribute():
    AttributeID: str
    PositionCode: Optional[str] #code
    DescriptionCode: Optional[str] #code
    Description: Optional[List[str]] #multiple instances possible

@dataclass 
class SellersItemIdentification():
    ID: str
    ExtendedID: Optional[str]
    PhysicalAttribute: Optional[List[PhysicalAttribute]] #multiple instances possible
    MeasurementDimension: Optional[List[Dimension]] #multiple instances possible
    IssuerParty: Optional[Party]

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
class PriceList():
    ID: Optional[str]
    StatusCode: Optional[str] # code
    ValidityPeriod: Optional[List[Period]] #multiple instances possible
    PreviousPriceList: Optional['PriceList']

@dataclass 
class Price(): #!
    PriceAmount: float #datatype: amount
    BaseQuantity: Optional[float] #datatype: quantity 
    PriceChangeReason: Optional[List[str]] #multiple instances possible
    PriceTypeCode: Optional[str] # code
    PriceType: Optional[str] 
    OrderableUnitFactorRate: Optional[float] #rate
    ValidityPeriod: Optional[List[Period]] #multiple instances possible
    PriceList: Optional[PriceList]
    AllowanceCharge: Optional[List[AllowanceCharge]] #multiple instances possible
    PricingExchangeRate: PricingExchangeRate

@dataclass 
class ItemPropertyGroup():
    ID: str 
    Name: Optional[str] # name
    ImportanceCode: Optional[str] # code

@dataclass 
class HazardousGoodsTransit():
    TransportEmergencyCardCode: Optional[str] # code
    PackingCriteriaCode: Optional[str] # code
    HazardousRegulationCode: Optional[str] # code
    InhalationToxicityZoneCode: Optional[str] # code
    TransportAuthorizationCode: Optional[str] # code
    MaximumTemperature: Optional[Temperature]
    MinimumTemperature: Optional[Temperature]

@dataclass 
class SecondaryHazard():
    ID: Optional[str]
    PlacardNotation: Optional[str]     
    PlacardEndorsement: Optional[str] 
    EmergencyProceduresCode: Optional[str] # code
    Extension: Optional[str]

@dataclass 
class CommodityClassification():
    NatureCode: Optional[str] # code
    CargoTypeCode: Optional[str] # code
    CommodityCode: Optional[str] # code
    ItemClassificationCode: Optional[str] # code

@dataclass 
class TransactionConditions():
    ID: Optional[str]
    ActionCode: Optional[str] # code
    Description: Optional[List[str]] #multiple instances possible
    DocumentReference: Optional[List[DocumentReference]] #multiple instances possible

@dataclass 
class ItemProperty():
    Name: Optional[str] # name
    NameCode: Optional[str] # code
    Value: Optional[str] #multiple instances possible
    ValueQuantity: Optional[float] #datatype: quantity
    Value: Optional[str] #multiple instances possible
    ImportanceCode: Optional[str] # code
    UsabilityPeriod: Optional[Period]
    ItemPropertyGroup: Optional[List[ItemPropertyGroup]] #multiple instances possible
    RangeDimension: Optional[Dimension]

@dataclass 
class HazardousItem():
    ID: Optional[str]
    PlacardNotation: Optional[str] 
    PlacardEndorsement: Optional[str] 
    AdditionalInformation: Optional[str] 
    UNDGCode: Optional[str] # code
    EmergencyProceduresCode: Optional[str] # code
    MedicalFirstAidGuideCode: Optional[str] # code
    TechnicalName: Optional[str] # name
    CategoryName: Optional[str] # name
    HazardousCategoryCode: Optional[str] # code
    UpperOrangeHazardPlacardID: Optional[str]
    LowerOrangeHazardPlacardID: Optional[str]
    MarkingID: Optional[str]
    HazardClassID: Optional[str]
    NetWeightMeasure: Optional[float] #measure Type
    NetVolumeMeasure: Optional[float] #measure Type
    Quantity: Optional[float] #datatype: quantity
    ContactParty: Optional[Party]
    SecondaryHazard: Optional[List[SecondaryHazard]] #multiple instances possible
    HazardousGoodsTransit: Optional[List[HazardousGoodsTransit]] #multiple instances possible
    EmergencyTemperature: Optional[Temperature]
    FlashpointTemperature: Optional[Temperature]
    AdditionalTemperature: Optional[List[Temperature]] #multiple instances possible

@dataclass 
class LotIdentification():
    LotNumberID: Optional[str]
    ExpiryDate: Optional[date] 
    AdditionalItemProperty: Optional[List[ItemProperty]] #multiple instances possible

@dataclass 
class ItemInstance():
    ProductTraceID: Optional[str]
    ManufactureDate: Optional[date] 
    ManufactureTime: Optional[time]   
    BestBeforeDate: Optional[date] 
    RegistrationID: Optional[str] 
    SerialID: Optional[str] 
    AdditionalItemProperty: Optional[List[ItemProperty]] #multiple instances possible
    LotIdentification: Optional[LotIdentification]

@dataclass 
class Item():
    Description: Optional[List[str]] #multiple instances possible
    PackQuantity: Optional[float] #datatype: quantity
    PackSizeNumeric: Optional[float] #numeric
    CatalogueIndicator: Optional[bool]
    Name: str # name
    HazardousRiskIndicator: Optional[bool]
    AdditionalInformation: Optional[str]
    Keyword: Optional[str]
    BrandName: Optional[str] # name
    ModelName: Optional[str] # name
    BuyersItemIdentification: Optional[BuyersItemIdentification]
    SellersItemIdentification: Optional[SellersItemIdentification]
    ManufacturersItemIdentification: Optional[ManufacturersItemIdentification]
    StandardItemIdentification: Optional[StandardItemIdentification]
    CatalogueItemIdentification: Optional[CatalogueItemIdentification]
    AdditionalItemIdentification: Optional[AdditionalItemIdentification]
    CatalogueDocumentReference: Optional[DocumentReference]
    ItemSpecificationDocumentReference: Optional[DocumentReference]
    OriginCountry: Optional[Country]
    CommodityClassification: Optional[List[CommodityClassification]] #multiple instances possible
    TransactionConditions: Optional[List[TransactionConditions]] #multiple instances possible
    HazardousItem: Optional[List[HazardousItem]] #multiple instances possible
    ClassifiedTaxCategory: Optional[List[TaxCategory]] #multiple instances possible
    AdditionalItemProperty: Optional[List[ItemProperty]] #multiple instances possible
    ManufacturerParty: Optional[List[Party]] #multiple instances possible
    InformationContentProviderParty: Optional[Party]
    OriginAddress: Optional[Address]
    ItemInstance: Optional[List[ItemInstance]] #multiple instances possible

@dataclass 
class TransportEquipmentSeal():
    ID: str
    SealIssuerTypeCode: Optional[str] # code
    Condition: Optional[str]
    SealStatusCode: Optional[str] # code
    SealingPartyType: Optional[str]

@dataclass 
class TransportEquipment():
    ID: Optional[str]
    TransportEquipmentTypeCode: Optional[str] # code
    ProviderTypeCode: Optional[str] # code
    OwnerTypeCode: Optional[str] # code
    SizeTypeCode: Optional[str] # code
    DispositionCode: Optional[str] # code
    FullnessIndicationCode: Optional[str] # code
    RefrigerationOnIndicator: Optional[bool]
    Information: Optional[str]
    ReturnabilityIndicator: Optional[bool]
    LegalStatusIndicator: Optional[bool]
    MeasurementDimension: Optional[List[Dimension]] #multiple instances possible
    TransportEquipmentSeal: Optional[List[TransportEquipmentSeal]] #multiple instances possible
    MinimumTemperature: Optional[Temperature]
    MaximumTemperature: Optional[Temperature]
    ProviderParty: Optional[Party] 
    LoadingProofParty: Optional[Party] 
    LoadingLocation: Optional[Location]
   
@dataclass 
class GoodsItemContainer():
    ID: str
    Quantity: Optional[float] #datatype: quantity
    TransportEquipment: Optional[List[TransportEquipment]] #multiple instances possible

@dataclass 
class GoodsItem():
    ID: str
    SequenceNumberID: Optional[str]
    Description: Optional[List[str]] #multiple instances possible
    HazardousRiskIndicator: Optional[bool]
    DeclaredCustomsValueAmount: Optional[float] #datatype: amount
    DeclaredForCarriageValueAmount: Optional[float] #datatype: amount
    DeclaredStatisticsValueAmount: Optional[float] #datatype: amount
    FreeOnBoardValueAmount: Optional[float] #datatype: amount
    InsuranceValueAmount: Optional[float] #datatype: amount
    ValueAmount: Optional[float] #datatype: amount
    GrossWeightMeasure: Optional[float] #measure Type   
    NetWeightMeasure: Optional[float] #measure Type   
    NetNetWeightMeasure: Optional[float] #measure Type   
    ChargeableWeightMeasure: Optional[float] #measure Type   
    GrossVolumeMeasure: Optional[float] #measure Type   
    NetVolumeMeasure: Optional[float] #measure Type   
    Quantity: Optional[float] #datatype: quantity
    PreferenceCriterionCode: Optional[str] # code
    RequiredCustomsID: Optional[str]
    CustomsStatusCode: Optional[str] # code
    CustomsTariffQuantity: Optional[float] #datatype: quantity
    CustomsImportClassifiedIndicator: Optional[bool]
    Item: Optional[List[Item]] #multiple instances possible
    GoodsItemContainer: Optional[List[GoodsItemContainer]] #multiple instances possible
    FreightAllowanceCharge: Optional[List[AllowanceCharge]] #multiple instances possible
    InvoiceLine: Optional['InvoiceLine']
    Temperature: Optional[List[Temperature]] #multiple instances possible
    ContainedGoodsItem : Optional['GoodsItem']
    OriginAddress: Optional[Address]
    
@dataclass 
class DeliveryUnit():
    BatchQuantity: float #datatype: quantity
    ConsumerUnitQuantity: Optional[float] #datatype: quantity
    HazardousRiskIndicator: Optional[bool]

@dataclass 
class Package():
    ID: Optional[str]
    Quantity: Optional[float] #datatype: quantity
    ReturnableMaterialIndicator: Optional[bool]
    PackageLevelCode: Optional[str] # code
    PackagingTypeCode: Optional[str] # code
    PackingMaterial: Optional[List[str]] #multiple instances possible
    ContainedPackage: Optional['Package']
    GoodsItem: Optional[List[GoodsItem]] #multiple instances possible
    MeasurementDimension: Optional[List[Dimension]] #multiple instances possible
    DeliveryUnit: Optional[List[DeliveryUnit]] #multiple instances possible

@dataclass 
class ItemLocationQuantity():
    LeadTimeMeasure: Optional[float] #measure Type   
    MinimumQuantity: Optional[float] #datatype: quantity
    MaximumQuantity: Optional[float] #datatype: quantity
    HazardousRiskIndicator: Optional[bool]
    TradingRestrictions: Optional[List[str]] #multiple instances possible
    ApplicableTerritoryAddress: Optional[List[Address]] #multiple instances possible
    Price: Optional[Price]
    DeliveryUnit: Optional[List[DeliveryUnit]] #multiple instances possible
    ApplicableTaxCategory: Optional[List[TaxCategory]] #multiple instances possible
    Package: Optional[Package]

@dataclass 
class PricingReference():
    OriginalItemLocationQuantity: Optional[ItemLocationQuantity]
    AlternativeConditionPrice: Optional[List[Price]] #multiple instances possible

@dataclass 
class OrderReference():
    ID: str
    SalesOrderID: Optional[str] 
    CopyIndicator: Optional[bool]
    UUID: Optional[str] 
    IssueDate: Optional[date] #date type (yyyy-mm-dd)
    IssueTime: Optional[time] #time type (00:00:00)
    SalesOrderID: Optional[str] 
    CustomerReference: Optional[str]
    DocumentReference: Optional[DocumentReference]

@dataclass 
class LineReference():
    LineID: str
    UUID: Optional[str] 
    LineStatusCode: Optional[str] #datatype: code
    DocumentReference: Optional[DocumentReference]

@dataclass 
class OrderLineReference():
    LineID: str
    SalesOrderLineID: Optional[str]
    UUID: Optional[str] 
    LineStatusCode: Optional[str] #datatype: code
    OrderReference: Optional[OrderReference]

@dataclass 
class TradeFinancing():
    ID: Optional[str]
    FinancingInstrumentCode: Optional[List[str]] #code #multiple instances possible
    ClauseCode: Optional[List[str]] #code #multiple instances possible
    Clause: Optional[List[str]] #multiple instances possible
    ContractDocumentReference: Optional[DocumentReference]
    DocumentReference: Optional[List[DocumentReference]] #multiple instances possible
    FinancingParty: Party
    FinancingFinancialAccount: Optional[FinancialAccount]
    
@dataclass 
class PaymentTerms():
    ID: Optional[str]
    PaymentMeansID: Optional[List[str]] #multiple instances possible
    PrepaidPaymentReferenceID: Optional[str]
    Note: Optional[List[str]] #multiple instances possible
    ReferenceEventCode: Optional[str] #datatype: code
    SettlementDiscountPercent: Optional[str] #Percent Type
    PenaltySurchargePercent: Optional[str] #Percent Type
    PaymentPercent: Optional[str] #Percent Type
    Amount: Optional[float] #datatype: amount
    SettlementDiscountAmount: Optional[float] #datatype: amount
    PenaltyAmount: Optional[float] #datatype: amount
    PaymentDueDate: Optional[date]
    InstallmentDueDate: Optional[date]
    SettlementPeriod: Optional[Period]
    PenaltyPeriod: Optional[Period]
    TradeFinancing: Optional[TradeFinancing]

@dataclass 
class InvoiceLine():
    ID: str 
    UUID: Optional[str]
    Note: Optional[str] 
    InvoicedQuantity: float #datatype: quantity
    LineExtensionAmount: float #datatype: amount
    TaxPointDate: Optional[date]
    AccountingCostCode: Optional[str] #datatype: code
    AccountingCost: Optional[str]
    FreeOfChargeIndicator: Optional[bool]
    OrderLineReference: Optional[OrderLineReference]
    DespatchLineReference: Optional[List[LineReference]] #multiple instances possible
    ReceiptLineReference: Optional[List[LineReference]] #multiple instances possible
    BillingReference: Optional[List[BillingReference]] #multiple instances possible
    PricingReference: Optional[PricingReference] 
    DocumentReference: Optional[List[DocumentReference]] #multiple instances possible
    OriginatorParty: Optional[Party] 
    Delivery: Optional[List[Delivery]] #multiple instances possible
    AllowanceCharge: Optional[List[AllowanceCharge]] #multiple instances possible
    TaxTotal: List[TaxTotal] #multiple instances possible
    Item: Item 
    Price: Price

@dataclass 
class UBLExtension(): #?????????????????????????????`?????????????```?`?????`
    ID: Optional[str]
    Name: Optional[str] #datatype: name
    ExtensionAgencyID: Optional[str]
    ExtensionAgencyName: Optional[str] #datatype: name
    ExtensionVersionID: Optional[str]
    ExtensionAgencyURI: Optional[str]
    ExtensionURI: Optional[str]
    ExtensionReasonCode: Optional[str] #code
    ExtensionReason: Optional[str]
    ExtensionContent: str 

@dataclass 
class UBLExtensions():
    UBLExtension: List[UBLExtension] #multiple instances possible

@dataclass #provide automatic generation of __init__(), among other things
class Invoice():
    UBLExtensions: Optional[UBLExtensions]
    UBLVersionID: str # identifier
    CustomizationID: str
    ProfileID: str
    ID: str
    CopyIndicator: Optional[bool]
    UUID: Optional[str]
    IssueDate: date #date type (yyyy-mm-dd)
    IssueTime: Optional[time] #time type (00:00:00)
    InvoiceTypeCode: Optional[str] #code type (example doc has e.g. 380 and DKK, so string to generalize)
    Note: Optional[List[str]] #multiple instances possible List[str] - list of?
    TaxPointDate: Optional[date]
    DocumentCurrencyCode: str #code
    TaxCurrencyCode: Optional[str] #code
    PricingCurrencyCode: Optional[str] # code
    PaymentCurrencyCode: Optional[str] # code
    PaymentAlternativeCurrencyCode: Optional[str] # code
    AccountingCostCode: Optional[str] #code
    AccountingCost: Optional[str]
    LineCountNumeric: Optional[float] #numeric: int?
    InvoicePeriod: Optional[Period]
    OrderReference: Optional[OrderReference]
    BillingReference: Optional[List[BillingReference]] # multiple instances possible
    DespatchDocumentReference: Optional[List[DocumentReference]] # multiple instances possible
    ReceiptDocumentReference: Optional[List[DocumentReference]] # multiple instances possible
    OriginatorDocumentReference: Optional[List[DocumentReference]] # multiple instances possible
    ContractDocumentReference: Optional[DocumentReference] 
    AdditionalDocumentReference: Optional[List[DocumentReference]] # multiple instances possible
    Signature: Optional[List[Signature]] # - multiple instances possible
    AccountingSupplierParty: AccountingSupplierParty
    AccountingCustomerParty: AccountingCustomerParty
    PayeeParty: Optional[PayeeParty]
    BuyerCustomerParty: Optional[BuyerCustomerParty]
    SellerSupplierParty: Optional[SellerSupplierParty]
    Delivery: Optional[List[Delivery]] #- multiple instances possible
    DeliveryTerms: Optional[DeliveryTerms]
    PaymentMeans: Optional[List[PaymentMeans]] # - multiple instances possible
    PaymentTerms: Optional[List[PaymentTerms]] # - multiple instances possible
    PrepaidPayment: Optional[List[Payment]] # - multiple instances possible
    AllowanceCharge: Optional[List[AllowanceCharge]] # - multiple instances possible
    TaxExchangeRate: Optional[TaxExchangeRate]
    PricingExchangeRate: Optional[PricingExchangeRate]
    PaymentExchangeRate: Optional[PaymentExchangeRate]
    PaymentAlternativeExchangeRate: Optional[PaymentAlternativeExchangeRate]
    TaxTotal: List[TaxTotal] # - multiple instances possible
    LegalMonetaryTotal: LegalMonetaryTotal
    InvoiceLine: List[InvoiceLine] # - multiple instances possible


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
'DeliveryLocation': Location,
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
'MinimumTemperature': Temperature,
'ItemPropertyGroup': ItemPropertyGroup,
'MeasurementDimension': Dimension,
'RangeDimension': Dimension,
'OriginalItemLocationQuantity': ItemLocationQuantity,
'Package': Package,
'DeliveryUnit': DeliveryUnit,
'ApplicableTerritoryAddress': Address,
'ApplicableTaxCategory': TaxCategory,
'ContainedPackage': Package,
'GoodsItem': GoodsItem,
'FreightAllowanceCharge': AllowanceCharge,
'Temperature': Temperature,
'ContainedGoodsItem': GoodsItem,
'GoodsItemContainer': GoodsItemContainer,
'TransportEquipment': TransportEquipment,
'ProviderParty': Party,
'LoadingProofParty': Party,
'LoadingLocation': Location,
'TransportEquipmentSeal': TransportEquipmentSeal,
'PriceList': PriceList,
'PreviousPriceList': PriceList,
'PhysicalAttribute': PhysicalAttribute,
'DeliveryContact': Contact,
'AccountingContact': Contact,
'BuyerContact': Contact,
'DespatchContact': Contact,
'SellerContact': Contact,
'Despatch': Despatch,
'DespatchAddress': Address,
'DespatchParty': Party,
'PhysicalLocation': Location,
'Person': Person,
'Language': Language,
'CorporateRegistrationScheme': CorporateRegistrationScheme,
'ExternalReference': ExternalReference,
'CreditAccount': CreditAccount,
'CardAccount': CardAccount,
'FinancialInstitution': FinancialInstitution,
'TradeFinancing': TradeFinancing,
'FinancingParty': Party,
'FinancingFinancialAccount': FinancialAccount,
'LocationCoordinate': LocationCoordinate,
'AddressLine': AddressLine,
'ContactParty': Party,
'UsabilityPeriod': Period,
'AlternativeConditionPrice': Price
}
