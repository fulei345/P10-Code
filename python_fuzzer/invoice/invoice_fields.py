fields = [
    ("UBLVersionID", "Identifier"),
    ("CustomizationID", "Identifier"),
    ("ProfileID", "Identifier"),
    ("ID", "Identifier"),
    ("CopyIndicator", "Indicator"),
    ("UUID", "Identifier"),
    ("IssueDate", "Date"),
    ("IssueTime", "Time"),
    ("InvoiceTypeCode", "Code"),
    ("Note", "Text"),
    ("TaxPointDate", "Date"),
    ("DocumentCurrencyCode", "Code"),
    ("TaxCurrencyCode", "Code"),
    ("PricingCurrencyCode", "Code"),
    ("PaymentCurrencyCode", "Code"),
    ("PaymentAlternativeCurrencyCode", "Code"),
    ("AccountingCostCode", "Code"),
    ("AccountingCost", "Text"),
    ("LineCountNumeric", "Numeric"),
    # UBLExtensions
    # InvoicePeriod
    # OrderReference
        #("ID", "Identifier"),
        #("CopyIndicator", "Indicator"),
        #("UUID", "Identifier"),
        #("IssueDate", "Date"),
        #("IssueTime", "Time"),
        ("SalesOrderID", "Identifier"),
        ("CustomerReference", "Text"),
        # DocumentReference 
            #("ID", "Identifier"),
            #("CopyIndicator", "Indicator"),
            #("UUID", "Identifier"),
            #("IssueDate", "Date"),
            ("XPath", "Text"),
            #Attachment
                ("EmbeddedDocumentBinaryObject", "Binary Object"),
                #ExternalReference
    # BillingReference
        #InvoiceDocumentReference
            #("ID", "Identifier"),
            #("CopyIndicator", "Indicator"),
            #("UUID", "Identifier"),
            #("IssueDate", "Date"),
            #("XPath", "Text"),
            #Attachment
        #SelfBilledInvoiceDocumentReference
            #("ID", "Identifier"),
            #("CopyIndicator", "Indicator"),
            #("UUID", "Identifier"),
            #("IssueDate", "Date"),
            #("XPath", "Text"),
            #Attachment
        #CreditNoteDocumentReference
            #("ID", "Identifier"),
            #("CopyIndicator", "Indicator"),
            #("UUID", "Identifier"),
            #("IssueDate", "Date"),
            #("XPath", "Text"),
            #Attachment
        #SelfBilledCreditNoteDocumentReference
            #("ID", "Identifier"),
            #("CopyIndicator", "Indicator"),
            #("UUID", "Identifier"),
            #("IssueDate", "Date"),
            #("XPath", "Text"),
            #Attachment
        #ReminderDocumentReference
            #("ID", "Identifier"),
            #("CopyIndicator", "Indicator"),
            #("UUID", "Identifier"),
            #("IssueDate", "Date"),
            #("XPath", "Text"),
            #Attachment
    # DespatchDocumentReference
        #("ID", "Identifier"),
        #("CopyIndicator", "Indicator"),
        #("UUID", "Identifier"),
        #("IssueDate", "Date"),
        #("XPath", "Text"),
        #Attachment
    # ReceiptDocumentReference
        #("ID", "Identifier"),
        #("CopyIndicator", "Indicator"),
        #("UUID", "Identifier"),
        #("IssueDate", "Date"),
        #("XPath", "Text"),
        #Attachment
    # OriginatorDocumentReference
        #("ID", "Identifier"),
        #("CopyIndicator", "Indicator"),
        #("UUID", "Identifier"),
        #("IssueDate", "Date"),
        #("XPath", "Text"),
        #Attachment
    # ContractDocumentReference
        #("ID", "Identifier"),
        #("CopyIndicator", "Indicator"),
        #("UUID", "Identifier"),
        #("IssueDate", "Date"),
        #("XPath", "Text"),
        #Attachment
    # AdditionalDocumentReference 
    # Signature 
    # AccountingSupplierParty
        ("CustomerAssignedAccountID", "Identifier"),
        ("AdditionalAccountID", "Identifier"),
        #Party 
            ("WebsiteURI", "Identifier"),
            ("LogoReferenceID", "Identifier"),
            ("EndpointID", "Identifier"),
            #PartyIdentification
            #PartyName
            #Language
            #PostalAddress
            #PhysicalLocation
            #PartyTaxScheme
            #PartyLegalEntity
            #Contact
            #Person
        #DespatchContact
        #AccountingContact
        #SellerContact
    # AccountingCustomerParty
        #("CustomerAssignedAccountID", "Identifier"),
        ("SupplierAssignedAccountID", "Identifier"),
        #("AdditionalAccountID", "Identifier"),
        #Party ! +?:
            #Contact ^?
                #("ID", "Identifier"),
                ("Name", "Name"),
                ("Telephone", "Text"),
                ("Telefax", "Text"),
                ("ElectronicMail", "Text"),
                #("Note", "Text"),
                #OtherCommunication
        #DeliveryContact
        #AccountingContact
        #BuyerContact 
    # PayeeParty
        #("WebsiteURI", "Identifier"),
        #("LogoReferenceID", "Identifier"),
        #("EndpointID", "Identifier"),
        #PartyIdentification
        #PartyName
        #Language
        #PostalAddress
        #PhysicalLocation
        #PartyTaxScheme
        #PartyLegalEntity
        #Contact 
        #Person
    # BuyerCustomerParty
        #("CustomerAssignedAccountID", "Identifier"),
        #("SupplierAssignedAccountID", "Identifier"),
        #("AdditionalAccountID", "Identifier"),
        #Party !
        #DeliveryContact
        #AccountingContact
        #BuyerContact 
    # SellerSupplierParty
        #("CustomerAssignedAccountID", "Identifier"),
        #("AdditionalAccountID", "Identifier"),
        #Party !
        #DespatchContact
        #AccountingContact
        #SellerContact
    # Delivery
        #("ID", "Identifier"),
        ("Quantity", "Quantity"),
        ("MinimumQuantity", "Quantity"),
        ("MaximumQuantity", "Quantity"),
        ("ActualDeliveryDate", "Date"),
        ("ActualDeliveryTime", "Time"),
        ("LatestDeliveryDate", "Date"),
        ("LatestDeliveryTime", "Time"),
        ("TrackingID", "Identifier"),
        #DeliveryLocation
        #RequestedDeliveryPeriod
        #DeliveryParty
        #Despatch
    # DeliveryTerms
        #("ID", "Identifier"),
        ("SpecialTerms", "Text"),
        ("LossRiskResponsibilityCode", "Code"),
        ("LossRisk", "Text"),
        #DeliveryLocation
            #("ID", "Identifier"),
            ("Description", "Text"),
            ("Conditions", "Text"),
            ("CountrySubentity", "Text"),
            ("CountrySubentityCode", "Code"),
            #ValidityPeriod
            #Address
    # PaymentMeans
    # PaymentTerms
    # PrepaidPayment
    # AllowanceCharge
    # TaxExchangeRate
        ("SourceCurrencyCode", "Code"),
        ("SourceCurrencyBaseRate", "Rate"),
        ("TargetCurrencyCode", "Code"),
        ("TargetCurrencyBaseRate", "Rate"),
        ("ExchangeMarketID", "Identifier"),
        ("CalculationRate", "Rate"),
        ("MathematicOperatorCode", "Code"),
        ("Date", "Date"),
        #ForeignExchangeContract
            #("ID", "Identifier"),
            #("IssueDate", "Date"),
            #("IssueTime", "Time"),
            ("ContractTypeCode", "Code"),
            ("ContractType", "Text"),
            #ValidityPeriod
            #ContractDocumentReference
                #("ID", "Identifier"),
                #("CopyIndicator", "Indicator"),
                #("UUID", "Identifier"),
                #("IssueDate", "Date"),
                #("XPath", "Text"),
                #Attachment !
    # PricingExchangeRate
        #("SourceCurrencyCode", "Code"),
        #("SourceCurrencyBaseRate", "Rate"),
        #("TargetCurrencyCode", "Code"),
        #("TargetCurrencyBaseRate", "Rate"),
        #("ExchangeMarketID", "Identifier"),
        #("CalculationRate", "Rate"),
        #("MathematicOperatorCode", "Code"),
        #("Date", "Date"),
        #ForeignExchangeContract !
    # PaymentExchangeRate
        #("SourceCurrencyCode", "Code"),
        #("SourceCurrencyBaseRate", "Rate"),
        #("TargetCurrencyCode", "Code"),
        #("TargetCurrencyBaseRate", "Rate"),
        #("ExchangeMarketID", "Identifier"),
        #("CalculationRate", "Rate"),
        #("MathematicOperatorCode", "Code"),
        #("Date", "Date"),
        #ForeignExchangeContract !
    # PaymentAlternativeExchangeRate
        #("SourceCurrencyCode", "Code"),
        #("SourceCurrencyBaseRate", "Rate"),
        #("TargetCurrencyCode", "Code"),
        #("TargetCurrencyBaseRate", "Rate"),
        #("ExchangeMarketID", "Identifier"),
        #("CalculationRate", "Rate"),
        #("MathematicOperatorCode", "Code"),
        #("Date", "Date"),
        #ForeignExchangeContract !
    # TaxTotal
    # LegalMonetaryTotal
    # InvoiceLine
        #("ID", "Identifier"),
        #("UUID", "Identifier"),
        #("Note", "Text"),
        ("InvoicedQuantity", "Quantity"),
        ("LineExtensionAmount", "Amount"),
        ("TaxPointDate", "Date"),
        ("AccountingCostCode", "Code"),
        ("AccountingCost", "Text"),
        ("FreeOfChargeIndicator", "Indicator"),
        #OrderLineReference
            ("LineID", "Identifier"),
            ("SalesOrderLineID", "Identifier"),
            #("UUID", "Identifier"),
            ("LineStatusCode", "Code"),
            #OrderReference !
        #DespatchLineReference
        #ReceiptLineReference
        #BillingReference !
        #PricingReference
        #DocumentReference !
        #OriginatorParty
        #Delivery !
        #AllowanceCharge 
        #TaxTotal
        #Item 
            #("Description", "Text"),
            ("PackQuantity", "Quantity"),
            ("PackSizeNumeric", "Numeric"),
            ("CatalogueIndicator", "Indicator"),
            #("Name", "Name"),
            ("HazardousRiskIndicator", "Indicator"),
            ("AdditionalInformation", "Text"),
            ("Keyword", "Text"), 
            ("BrandName", "Name"),
            ("ModelName", "Name"),
            #BuyersItemIdentification
                #("ID", "Identifier"),
                ("ExtendedID", "Identifier"),
                #IssuerParty
            #SellersItemIdentification
                #("ID", "Identifier"),
                #("ExtendedID", "Identifier"),
                #PhysicalAttribute
                #MeasurementDimension
                #IssuerParty
            #ManufacturersItemIdentification
                #("ID", "Identifier"),
                #("ExtendedID", "Identifier"),
                #IssuerParty
            #StandardItemIdentification
                #("ID", "Identifier"),
                #("ExtendedID", "Identifier"),
                #IssuerParty
            #CatalogueItemIdentification
                #("ID", "Identifier"),
                #("ExtendedID", "Identifier"),
                #IssuerParty
            #AdditionalItemIdentification
                #("ID", "Identifier"),
                #("ExtendedID", "Identifier"),
                #IssuerParty
            #CatalogueDocumentReference
                #("ID", "Identifier"),
                #("CopyIndicator", "Indicator"),
                #("UUID", "Identifier"),
                #("IssueDate", "Date"),
                #("XPath", "Text"),
                #Attachment
            #ItemSpecificationDocumentReference
            #OriginCountry
            #CommodityClassification
            #TransactionConditions
            #HazardousItem
            #ClassifiedTaxCategory
            #AdditionalItemProperty
            #ManufacturerParty
            #InformationContentProviderParty
            #OriginAddress
            #ItemInstance
        #Price
]