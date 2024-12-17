# Analytical Information Markup Language

An AnIML file (also called an instance in XML speak) is an XML representation of a piece of analytical data gathered from an instrument. The format of AnIML files is structured based off of a set of rules - a schema file (see 'Core Schema'). The schema dictates the elements (tags) allowed in the file, the data type of the information in the elements, and even (if required) what values are allowed within an element. If an AnIML file is written in accordance with the published schema it is said to be 'a valid instance file'.

The AnIML standard was developed to address the need for a universal data format in analytical chemistry and related fields. It provides a flexible yet structured way to store both raw experimental data and associated metadata. The format is designed to capture the complete context of an analytical measurement, including instrument parameters, sample information, measurement conditions, and results.

A key feature of AnIML is its hierarchical organization around ExperimentSteps, which represent distinct analytical procedures or measurements. Each ExperimentStep contains comprehensive information about the technique used, method parameters, and resulting data. This structure allows AnIML to effectively document complex analytical workflows involving multiple techniques and instruments.

The standard also includes robust support for data provenance through its AuditTrail system, which tracks all modifications made to an AnIML document. This ensures full traceability of the data lifecycle, from initial acquisition through any subsequent processing or analysis steps. Additionally, AnIML's Template system enables standardization of common experimental procedures while maintaining the flexibility to accommodate diverse analytical techniques.

- [Analytical Information Markup Language](#analytical-information-markup-language)
    - [AnIML](#animl)
    - [SampleSet](#sampleset)
    - [AuditTrailEntrySet](#audittrailentryset)
    - [ExperimentStepSet](#experimentstepset)
    - [Sample](#sample)
    - [AuditTrailEntry](#audittrailentry)
    - [Template](#template)
    - [ExperimentStep](#experimentstep)
    - [Diff](#diff)
    - [Author](#author)
    - [Software](#software)
    - [TagSet](#tagset)
    - [Result](#result)
    - [Method](#method)
    - [Technique](#technique)
    - [Infrastructure](#infrastructure)
    - [Tag](#tag)
    - [Category](#category)
    - [Device](#device)
    - [Extension](#extension)
    - [ExperimentDataReferenceSet](#experimentdatareferenceset)
    - [ParentDataPointReferenceSet](#parentdatapointreferenceset)
    - [SampleReferenceSet](#samplereferenceset)
    - [SeriesSet](#seriesset)
    - [Parameter](#parameter)
    - [ExperimentDataReference](#experimentdatareference)
    - [ExperimentDataBulkReference](#experimentdatabulkreference)
    - [ParentDataPointReference](#parentdatapointreference)
    - [SampleReference](#samplereference)
    - [SampleInheritance](#sampleinheritance)
    - [Series](#series)
    - [SIUnit](#siunit)
    - [EndValue](#endvalue)
    - [IndividualValueSet](#individualvalueset)
    - [Unit](#unit)
    - [AutoIncrementedValueSet](#autoincrementedvalueset)
    - [EncodedValueSet](#encodedvalueset)
    - [StartValue](#startvalue)
    - [Increment](#increment)

---

### AnIML

ComplexType for the root element of an AnIML document. The AnIML element serves as the container for all data and metadata in an analytical data file. It contains version information, sample definitions, experimental data organized in steps, and an audit trail of changes made to the document.

- **version**
  - Type: string
  - Description: Version number of the AnIML Core Schema used in this document. Must be '0.90'.
  - Default: 0.90
  - XML: @version
- sample_set
  - Type: [SampleSet](#SampleSet)
  - Description: Container for Samples used in this AnIML document.
  - XML: SampleSet
- experiment_step_set
  - Type: [ExperimentStepSet](#ExperimentStepSet)
  - Description: Container for multiple ExperimentSteps that describe the process and results.
  - XML: ExperimentStepSet
- audit_trail_entry_set
  - Type: [AuditTrailEntrySet](#AuditTrailEntrySet)
  - Description: Container for audit trail entries describing changes to this document.
  - XML: AuditTrailEntrySet

---

### SampleSet

Container for Samples used in this AnIML document. The SampleSet element acts as a registry of all samples referenced throughout the document, allowing samples to be defined once and referenced multiple times. This centralized approach ensures consistency in sample identification and properties across the entire analytical workflow.

- sample
  - Type: [Sample](#Sample)[]
  - Description: Individual Sample, referenced from other parts of this AnIML document.
  - XML: Sample

### AuditTrailEntrySet

Container for audit trail entries describing changes to this document. The AuditTrailEntrySet maintains a chronological record of all modifications made to the AnIML document, including who made the changes, when they were made, and what specific changes occurred. This provides full traceability and compliance with data integrity requirements.

- audit_trail_entry
  - Type: [AuditTrailEntry](#AuditTrailEntry)[]
  - Description: Describes a set of changes made to the particular AnIML document by one user at a given time.
  - XML: AuditTrailEntry

---

### ExperimentStepSet

Container for multiple ExperimentSteps that describe the process and results. The ExperimentStepSet organizes the analytical workflow into discrete steps, where each step represents the application of a specific analytical technique. This structure allows for clear documentation of complex, multi-step analytical procedures while maintaining relationships between steps.

- experiment_step
  - Type: [ExperimentStep](#ExperimentStep)[]
  - Description: Container that documents a step in an experiment. Use one ExperimentStep per application of a Technique.
  - XML: ExperimentStep
- template
  - Type: [Template](#Template)[]
  - Description: Represents a template for an ExperimentStep.
  - XML: Template

---

### Sample

Individual Sample, referenced from other parts of this AnIML document. The Sample element provides comprehensive documentation of a physical or virtual sample, including its identification, physical location, containment hierarchy, and any relevant metadata. It supports both simple samples and complex container-based sample organizations like well plates.

- **name**
  - Type: string
  - Description: Plain-text name of this item.
  - XML: @name
- **sample_id**
  - Type: string
  - Description: None
  - XML: @sampleID
- barcode
  - Type: string
  - Description: Value of barcode label that is attached to sample container.
  - XML: @barcode
- comment
  - Type: string
  - Description: Unstructured text comment to further describe the Sample.
  - XML: @comment
- derived
  - Type: string
  - Description: Indicates whether this is a derived Sample. A derived Sample is a Sample that has been created by applying a Technique. (Sub-Sampling, Processing, ...)
  - XML: @derived
- container_type
  - Type: string
  - Description: Whether this sample is also a container for other samples. Set to 'simple' if not.
  - XML: @containerType
- container_id
  - Type: string
  - Description: Sample ID of container in which this sample is located.
  - XML: @containerID
- location_in_container
  - Type: string
  - Description: Coordinates of this sample within the enclosing container. In case of microplates or trays, the row is identified by letters and the column is identified by numbers (1-based) while in landscape orientation. Examples: A10 = 1st row, 10th column, Z1 = 26th row, 1st column, AB2 = 28th row, 2nd column.
  - XML: @locationInContainer
- source_data_location
  - Type: string
  - Description: Points to the original data source. May be a file name, uri, database ID, etc.
  - XML: @sourceDataLocation
- tag_set
  - Type: [TagSet](#TagSet)
  - Description: Set of Tag elements.
  - XML: TagSet
- category
  - Type: [Category](#Category)
  - Multiple: True
  - Description: Defines a category of Parameters and SeriesSets. Used to model hierarchies.
  - XML: Category

---

### AuditTrailEntry

Describes a set of changes made to the particular AnIML document by one user at a given time. The AuditTrailEntry element captures the complete context of a document modification event, including who made the change, when it occurred, what software was used, and both human-readable and machine-readable descriptions of the changes. This enables full traceability of document history.

- **timestamp**
  - Type: string
  - Description: Date and time of modification.
  - XML: Timestamp
- **author**
  - Type: [Author](#Author)
  - Description: Information about a person, a device or a piece of software authoring AnIML files.
  - XML: Author
- **action**
  - Type: string
  - Description: Type of change made (created, modified, ...)
  - XML: Action
- software
  - Type: [Software](#Software)
  - Description: Software used to author this.
  - XML: Software
- reason
  - Type: string
  - Description: Explanation why changes were made.
  - XML: Reason
- comment
  - Type: string
  - Description: Human-readable comment further explaining the changes.
  - XML: Comment
- diff
  - Type: [Diff](#Diff)
  - Multiple: True
  - Description: Machine-readable description of changes made.
  - XML: Diff
- reference
  - Type: string
  - Multiple: True
  - Description: ID of the SignableItem that was affected. If none is specified, entire document is covered.
  - XML: Reference

---

### Template

Represents a template for an ExperimentStep. Templates provide a reusable pattern for creating ExperimentSteps with predefined structure and metadata. They help ensure consistency across similar experimental procedures.

- **name**
  - Type: string
  - Description: Plain-text name of this item.
  - XML: @name
- **template_id**
  - Type: string
  - Description: None
  - XML: @templateID
- source_data_location
  - Type: string
  - Description: Points to the original data source. May be a file name, uri, database ID, etc.
  - XML: @sourceDataLocation
- tag_set
  - Type: [TagSet](#TagSet)
  - Description: Set of Tag elements.
  - XML: TagSet
- technique
  - Type: [Technique](#Technique)
  - Description: Reference to Technique Definition used in this Experiment.
  - XML: Technique
- infrastructure
  - Type: [Infrastructure](#Infrastructure)
  - Description: Contains references to the context of this Experiment.
  - XML: Infrastructure
- method
  - Type: [Method](#Method)
  - Description: Describes how this Experiment was performed.
  - XML: Method
- result
  - Type: [Result](#Result)
  - Multiple: True
  - Description: Container for Data derived from Experiment.
  - XML: Result

---

### ExperimentStep

Container that documents a step in an experiment. Use one ExperimentStep per application of a Technique. ExperimentSteps are the fundamental building blocks of an AnIML document, capturing the complete context, method, and results of a single experimental procedure or measurement.

- **name**
  - Type: string
  - Description: Plain-text name of this item.
  - XML: @name
- **experiment_step_id**
  - Type: string
  - Description: Unique identifier for this ExperimentStep. Used to point to this step from an ExperimentDataReference.
  - XML: @experimentStepID
- template_used
  - Type: string
  - Description: None
  - XML: @templateUsed
- comment
  - Type: string
  - Description: Unstructured text comment to further describe the ExperimentStep.
  - XML: @comment
- source_data_location
  - Type: string
  - Description: Points to the original data source. May be a file name, uri, database ID, etc.
  - XML: @sourceDataLocation
- tag_set
  - Type: [TagSet](#TagSet)
  - Description: Set of Tag elements.
  - XML: TagSet
- technique
  - Type: [Technique](#Technique)
  - Description: Reference to Technique Definition used in this Experiment.
  - XML: Technique
- infrastructure
  - Type: [Infrastructure](#Infrastructure)
  - Description: Contains references to the context of this Experiment.
  - XML: Infrastructure
- method
  - Type: [Method](#Method)
  - Description: Describes how this Experiment was performed.
  - XML: Method
- result
  - Type: [Result](#Result)
  - Multiple: True
  - Description: Container for Data derived from Experiment.
  - XML: Result

---

### Diff

Machine-readable description of changes made. Diffs provide a detailed record of modifications made to an AnIML document, enabling precise tracking of what was changed, when, and by whom. This supports audit trails and change management requirements.

- **scope**
  - Type: string
  - Description: Scope of diff. May be 'element' or 'attribute'.
  - XML: @scope
- **changed_item**
  - Type: string
  - Description: ID of the SignableItem that was changed
  - XML: @changedItem
- **old_value**
  - Type: string
  - Description: No descripiton provided
  - XML: OldValue
- **new_value**
  - Type: string
  - Description: No descripiton provided
  - XML: NewValue

---

### Author

Information about a person, a device or a piece of software authoring AnIML files. Authors can be human users, automated systems, or software applications that create or modify AnIML documents. This flexible definition supports both manual and automated workflows while maintaining clear provenance.

- **user_type**
  - Type: string
  - Description: Type of user (human, device, software)
  - XML: @userType
- **name**
  - Type: string
  - Description: Common name.
  - XML: Name
- affiliation
  - Type: string
  - Description: Organization the Author is affiliated with.
  - XML: Affiliation
- role
  - Type: string
  - Description: Role the Author plays within the organization.
  - XML: Role
- email
  - Type: string
  - Description: RFC822-compliant email address.
  - XML: Email
- phone
  - Type: string
  - Description: Phone number.
  - XML: Phone
- location
  - Type: string
  - Description: Location or physical address.
  - XML: Location

---

### Software

Software used to author this. This element captures details about software applications involved in creating or modifying AnIML documents, including version information and operating environment details for reproducibility and troubleshooting.

- **name**
  - Type: string
  - Description: Common name.
  - XML: Name
- manufacturer
  - Type: string
  - Description: Company name.
  - XML: Manufacturer
- version
  - Type: string
  - Description: Version identifier of software release.
  - XML: Version
- operating_system
  - Type: string
  - Description: Operating system the software was running on.
  - XML: OperatingSystem

---

### TagSet

Set of Tag elements. TagSets provide a flexible mechanism for adding metadata and classifications to AnIML elements. They can be used to group related items, add external references, or implement custom categorization schemes.

- tag
  - Type: [Tag](#Tag)
  - Multiple: True
  - Description: Tag to mark related data items. When a value is given, it may also serve as a reference to an external data system.
  - XML: Tag

---

### Result

Container for Data derived from Experiment. Results store the actual experimental data along with its organization into series and categories. This structured approach allows for clear representation of both simple and complex multidimensional datasets.

- **name**
  - Type: string
  - Description: Plain-text name of this item.
  - XML: @name
- series_set
  - Type: [SeriesSet](#SeriesSet)
  - Description: Container for n-dimensional Data.
  - XML: SeriesSet
- category
  - Type: [Category](#Category)
  - Multiple: True
  - Description: Defines a category of Parameters and SeriesSets. Used to model hierarchies.
  - XML: Category

---

### Method

Describes how this Experiment was performed. Methods document the complete experimental procedure, including the people involved, equipment used, and software settings. This comprehensive record ensures experiments can be understood and potentially reproduced.

- name
  - Type: string
  - Description: Optional method name, as defined in the instrument software.
  - XML: @name
- author
  - Type: [Author](#Author)
  - Description: Information about a person, a device or a piece of software authoring AnIML files.
  - XML: Author
- device
  - Type: [Device](#Device)
  - Description: Device used to perform experiment.
  - XML: Device
- software
  - Type: [Software](#Software)
  - Description: Software used to author this.
  - XML: Software
- category
  - Type: [Category](#Category)
  - Multiple: True
  - Description: Defines a category of Parameters and SeriesSets. Used to model hierarchies.
  - XML: Category

---

### Technique

Reference to Technique Definition used in this Experiment. Techniques define the standardized structure and vocabulary for specific types of experimental procedures. This reference system ensures consistent data organization across different implementations of the same technique.

- **name**
  - Type: string
  - Description: Plain-text name of this item.
  - XML: @name
- **uri**
  - Type: string
  - Description: URI where Technique Definition file can be fetched.
  - XML: @uri
- sha256
  - Type: string
  - Description: SHA256 checksum of the referenced Technique Definition. Hex encoded, lower cased. Similar to the output of the sha256 unix command.
  - XML: @sha256
- extension
  - Type: [Extension](#Extension)
  - Multiple: True
  - Description: Reference to an Extension to amend the active Technique Definition.
  - XML: Extension

---

### Infrastructure

Contains references to the context of this Experiment. Infrastructure elements provide the broader experimental context by linking to samples, related experiments, and temporal information. This creates a web of relationships between different experimental components.

- sample_reference_set
  - Type: [SampleReferenceSet](#SampleReferenceSet)
  - Description: Set of Samples used in this Experiment.
  - XML: SampleReferenceSet
- parent_data_point_reference_set
  - Type: [ParentDataPointReferenceSet](#ParentDataPointReferenceSet)
  - Description: Contains references to the parent Result.
  - XML: ParentDataPointReferenceSet
- experiment_data_reference_set
  - Type: [ExperimentDataReferenceSet](#ExperimentDataReferenceSet)
  - Description: Set of Experiment Steps consumed by this Experiment Step.
  - XML: ExperimentDataReferenceSet
- timestamp
  - Type: string
  - Description: Date and time of modification.
  - XML: Timestamp

---

### Tag

Tag to mark related data items. When a value is given, it may also serve as a reference to an external data system. Tags provide a flexible way to add metadata, create groupings, or link to external systems while maintaining the structured nature of AnIML documents.

- **name**
  - Type: string
  - Description: None
  - XML: @name
- value
  - Type: string
  - Description: None
  - XML: @value

---

### Category

Defines a category of Parameters and SeriesSets. Used to model hierarchies. Categories enable logical grouping and organization of experimental data and parameters, supporting complex data structures while maintaining clear relationships between elements.

- **name**
  - Type: string
  - Description: Plain-text name of this item.
  - XML: @name
- parameter
  - Type: [Parameter](#Parameter)
  - Multiple: True
  - Description: Name/Value Pair.
  - XML: Parameter
- series_set
  - Type: [SeriesSet](#SeriesSet)
  - Multiple: True
  - Description: Container for n-dimensional Data.
  - XML: SeriesSet
- category
  - Type: [Category](#Category)
  - Multiple: True
  - Description: Defines a category of Parameters and SeriesSets. Used to model hierarchies.
  - XML: Category

---

### Device

Device used to perform experiment. This element captures detailed information about laboratory instruments and equipment used in experiments, supporting traceability and reproducibility requirements.

- **name**
  - Type: string
  - Description: Common name.
  - XML: Name
- device_identifier
  - Type: string
  - Description: Unique name or identifier of the device.
  - XML: DeviceIdentifier
- manufacturer
  - Type: string
  - Description: Company name.
  - XML: Manufacturer
- firmware_version
  - Type: string
  - Description: Version identifier of firmware release.
  - XML: FirmwareVersion
- serial_number
  - Type: string
  - Description: Unique serial number of device.
  - XML: SerialNumber

---

### Extension

Reference to an Extension to amend the active Technique Definition. Extensions allow for customization and enhancement of standard Technique Definitions while maintaining compatibility with the base specification.

- **uri**
  - Type: string
  - Description: URI where Extension file can be fetched.
  - XML: @uri
- **name**
  - Type: string
  - Description: Name of Extension to be used. Must match Name given in Extension Definition file.
  - XML: @name
- sha256
  - Type: string
  - Description: SHA256 checksum of the referenced Extension. Hex encoded, lower cased. Similar to the output of the sha256 unix command.
  - XML: @sha256

---

### ExperimentDataReferenceSet

Set of Experiment Steps consumed by this Experiment Step. This element manages dependencies between different experimental steps, allowing for complex workflows where the output of one step becomes input for another.

- experiment_data_reference
  - Type: [ExperimentDataReference](#ExperimentDataReference)
  - Multiple: True
  - Description: Reference to an Experiment Step whose data is consumed.
  - XML: ExperimentDataReference
- experiment_data_bulk_reference
  - Type: [ExperimentDataBulkReference](#ExperimentDataBulkReference)
  - Multiple: True
  - Description: Prefix-based reference to a set of Experiment Steps whose data are consumed.
  - XML: ExperimentDataBulkReference

---

### ParentDataPointReferenceSet

Contains references to the parent Result. This element enables precise linking between related data points across different experimental steps, supporting detailed tracking of data relationships and dependencies.

- **parent_data_point_reference**
  - Type: [ParentDataPointReference](#ParentDataPointReference)
  - Multiple: True
  - Description: Reference to a data point or value range in an independent Series in the parent Result.
  - XML: ParentDataPointReference

---

### SampleReferenceSet

Set of Samples used in this Experiment. This element manages relationships between experiments and samples, tracking both sample usage and sample transformations throughout experimental workflows.

- sample_reference
  - Type: [SampleReference](#SampleReference)
  - Multiple: True
  - Description: Reference to a Sample used in this Experiment.
  - XML: SampleReference
- sample_inheritance
  - Type: [SampleInheritance](#SampleInheritance)
  - Multiple: True
  - Description: Indicates that a Sample was inherited from the parent ExperimentStep.
  - XML: SampleInheritance

---

### SeriesSet

Container for n-dimensional Data. SeriesSets organize related data series into logical groups, supporting both simple linear data and complex multi-dimensional datasets while maintaining clear relationships between dependent and independent variables.

- **name**
  - Type: string
  - Description: Plain-text name of this item.
  - XML: @name
- **length**
  - Type: string
  - Description: Number of data points each Series contains.
  - XML: @length
- **series**
  - Type: [Series](#Series)
  - Multiple: True
  - Description: Container for multiple Values.
  - XML: Series

---

### Parameter

Name/Value Pair. Parameters store individual data points and experimental settings, supporting multiple data types and optional units for complete scientific documentation.

- **name**
  - Type: string
  - Description: Plain-text name of this item.
  - XML: @name
- **parameter_type**
  - Type: string
  - Description: Data type of this parameter
  - XML: @parameterType
- **value**
  - Type: integer, float, string, boolean
  - Description: I: Individual integer value (32 bits, signed). L: Individual long integer value (64 bits, signed). F: Individual 32-bit floating point value. D: Individual 64-bit floating point value. S: Individual string value. Boolean: Individual boolean value.
  - XML: I, F, S, Boolean
- unit
  - Type: [Unit](#Unit)
  - Description: Unit: Definition of a Scientific Unit.
  - XML: Unit: Unit

---

### ExperimentDataReference

Reference to an Experiment Step whose data is consumed. This element creates explicit links between experimental steps, documenting how data flows through multi-step experimental procedures.

- **role**
  - Type: string
  - Description: None
  - XML: @role
- **data_purpose**
  - Type: string
  - Description: None
  - XML: @dataPurpose
- **experiment_step_id**
  - Type: string
  - Description: None
  - XML: @experimentStepID

---

### ExperimentDataBulkReference

Prefix-based reference to a set of Experiment Steps whose data are consumed. This element enables efficient referencing of multiple related experimental steps through pattern matching.

- **role**
  - Type: string
  - Description: None
  - XML: @role
- **data_purpose**
  - Type: string
  - Description: None
  - XML: @dataPurpose
- **experiment_step_id_prefix**
  - Type: string
  - Description: None
  - XML: @experimentStepIDPrefix

---

### ParentDataPointReference

Reference to a data point or value range in an independent Series in the parent Result. This element enables precise linking between specific data points across different experimental steps.

- **series_id**
  - Type: string
  - Description: Contains the ID of the Series referenced.
  - XML: @seriesID
- **start_value**
  - Type: [StartValue](#StartValue)
  - Description: Lower boundary of an interval or ValueSet.
  - XML: StartValue
- end_value
  - Type: [EndValue](#EndValue)
  - Description: Upper boundary of an interval.
  - XML: EndValue

---

### SampleReference

Reference to a Sample used in this Experiment. This element creates explicit links between experiments and samples, documenting how samples are used or transformed during experimental procedures.

- **sample_id**
  - Type: string
  - Description: SampleID of the Sample used in the current ExperimentStep. Refers to the sampleID within the SampleSet section of the document.
  - XML: @sampleID
- **role**
  - Type: string
  - Description: Role this sample plays within the current ExperimentStep.
  - XML: @role
- **sample_purpose**
  - Type: string
  - Description: Specifies whether the referenced sample is produced or consumed by the current ExperimentStep.
  - XML: @samplePurpose

---

### SampleInheritance

Indicates that a Sample was inherited from the parent ExperimentStep. This element supports tracking sample lineage through multi-step experimental procedures.

- **role**
  - Type: string
  - Description: Role this sample plays within the current ExperimentStep.
  - XML: @role
- **sample_purpose**
  - Type: string
  - Description: Specifies whether the referenced sample is produced or consumed by the current ExperimentStep.
  - XML: @samplePurpose

---

### Series

Container for multiple Values. Series elements store ordered collections of data points, supporting multiple data types and optional units while maintaining relationships between dependent and independent variables.

- **name**
  - Type: string
  - Description: Plain-text name of this item.
  - XML: @name
- **dependency**
  - Type: string
  - Description: Specified whether the Series is independent or dependent.
  - XML: @dependency
- **series_id**
  - Type: string
  - Description: Identifies the Series. Used in References from subordinate ExperimentSteps. Unique per SeriesSet.
  - XML: @seriesID
- **series_type**
  - Type: string
  - Description: Data type used by all values in this Series.
  - XML: @seriesType
- visible
  - Type: string
  - Description: Specifies whether data in this Series is to be displayed to the user by default.
  - XML: @visible
- plot_scale
  - Type: string
  - Description: Specifies whether the data in this Series is typically plotted on a linear or logarithmic scale.
  - XML: @plotScale
- value_set
  - Type: IndividualValueSet, EncodedValueSet, AutoIncrementedValueSet
  - Description: IndividualValueSet: Multiple Values explicitly specified. EncodedValueSet: Multiple numeric values encoded as a base64 binary string. Uses little-endian byte order. AutoIncrementedValueSet: Multiple values given in form of a start value and an increment.
  - XML: IndividualValueSet, EncodedValueSet, AutoIncrementedValueSet
- unit
  - Type: [Unit](#Unit)
  - Description: Definition of a Scientific Unit.
  - XML: Unit

---

### SIUnit

Combination of SI Units used to represent Scientific unit. This element enables precise specification of complex scientific units through combinations of base SI units.

- factor
  - Type: string
  - Description: None
  - XML: @factor
- exponent
  - Type: string
  - Description: None
  - XML: @exponent
- offset
  - Type: string
  - Description: None
  - XML: @offset

---

### EndValue

Upper boundary of an interval. This element works with StartValue to define precise numeric ranges for data selection and reference.

- **value**
  - Type: integer, float
  - Description: I: Individual integer value (32 bits, signed). L: Individual long integer value (64 bits, signed). F: Individual 32-bit floating point value. D: Individual 64-bit floating point value.
  - XML: I, F

---

### IndividualValueSet

Multiple Values explicitly specified. This element provides direct storage of data values, supporting multiple data types for maximum flexibility.

- **values**
  - Type: float, integer, string, boolean
  - Multiple: True
  - Description: I: Individual integer value (32 bits, signed). L: Individual long integer value (64 bits, signed). F: Individual 32-bit floating point value. D: Individual 64-bit floating point value. S: Individual string value. Boolean: Individual boolean value.
  - XML: I, F, S, Boolean
- start_index
  - Type: string
  - Description: Zero-based index of the first entry in this Value Set. The specification is inclusive.
  - XML: @startIndex
- end_index
  - Type: string
  - Description: Zero-based index of the last entry in this Value Set. The specification is inclusive.
  - XML: @endIndex

---

### Unit

Definition of a Scientific Unit. This element provides a structured way to specify scientific units, supporting both simple units and complex combinations of SI units.

- **label**
  - Type: string
  - Description: Defines the visual representation of a particular Unit.
  - XML: @label
- quantity
  - Type: string
  - Description: Quantity the unit can be applied to
  - XML: @quantity
- si_unit
  - Type: [SIUnit](#SIUnit)
  - Multiple: True
  - Description: Combination of SI Units used to represent Scientific unit
  - XML: SIUnit

---

### AutoIncrementedValueSet

Multiple values given in form of a start value and an increment. This element provides an efficient way to represent regular sequences of numeric values without storing each individual value.

- **start_value**
  - Type: [StartValue](#StartValue)
  - Description: Lower boundary of an interval or ValueSet.
  - XML: StartValue
- **increment**
  - Type: [Increment](#Increment)
  - Description: Increment value
  - XML: Increment
- start_index
  - Type: string
  - Description: Zero-based index of the first entry in this Value Set. The specification is inclusive.
  - XML: @startIndex
- end_index
  - Type: string
  - Description: Zero-based index of the last entry in this Value Set. The specification is inclusive.
  - XML: @endIndex

---

### EncodedValueSet

Multiple numeric values encoded as a base64 binary string. Uses little-endian byte order. This element provides efficient storage of large numeric datasets through binary encoding.

- start_index
  - Type: string
  - Description: Zero-based index of the first entry in this Value Set. The specification is inclusive.
  - XML: @startIndex
- end_index
  - Type: string
  - Description: Zero-based index of the last entry in this Value Set. The specification is inclusive.
  - XML: @endIndex

---

### StartValue

Lower boundary of an interval or ValueSet. This element works with EndValue to define precise numeric ranges for data selection and reference.

- **value**
  - Type: integer, float
  - Description: I: Individual integer value (32 bits, signed). L: Individual long integer value (64 bits, signed). F: Individual 32-bit floating point value. D: Individual 64-bit floating point value.
  - XML: I, F

---

### Increment

Increment value. This element specifies the step size for AutoIncrementedValueSets, enabling efficient representation of regular numeric sequences.

- **value**
  - Type: integer, float
  - Description: I: Individual integer value (32 bits, signed). L: Individual long integer value (64 bits, signed). F: Individual 32-bit floating point value. D: Individual 64-bit floating point value.
  - XML: I, F
