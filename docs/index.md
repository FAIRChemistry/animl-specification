---
hide:
    - navigation
---

# Analytical Information Markup Language

This page provides comprehensive information about the structure and components of the data model, including detailed descriptions of the types and their properties, information on enumerations, and an overview of the ontologies used and their associated prefixes. Below, you will find a graph that visually represents the overall structure of the data model.

??? quote "Graph"
    ``` mermaid
    flowchart TB
        animl(AnIML)
        sampleset(SampleSet)
        audittrailentryset(AuditTrailEntrySet)
        experimentstepset(ExperimentStepSet)
        sample(Sample)
        audittrailentry(AuditTrailEntry)
        template(Template)
        experimentstep(ExperimentStep)
        diff(Diff)
        author(Author)
        software(Software)
        tagset(TagSet)
        result(Result)
        method(Method)
        technique(Technique)
        infrastructure(Infrastructure)
        tag(Tag)
        category(Category)
        device(Device)
        extension(Extension)
        experimentdatareferenceset(ExperimentDataReferenceSet)
        parentdatapointreferenceset(ParentDataPointReferenceSet)
        samplereferenceset(SampleReferenceSet)
        seriesset(SeriesSet)
        parameter(Parameter)
        experimentdatareference(ExperimentDataReference)
        experimentdatabulkreference(ExperimentDataBulkReference)
        parentdatapointreference(ParentDataPointReference)
        samplereference(SampleReference)
        sampleinheritance(SampleInheritance)
        series(Series)
        siunit(SIUnit)
        endvalue(EndValue)
        individualvalueset(IndividualValueSet)
        unit(Unit)
        autoincrementedvalueset(AutoIncrementedValueSet)
        encodedvalueset(EncodedValueSet)
        startvalue(StartValue)
        increment(Increment)
        animl(AnIML) --> sampleset(SampleSet)
        animl(AnIML) --> experimentstepset(ExperimentStepSet)
        animl(AnIML) --> audittrailentryset(AuditTrailEntrySet)
        sampleset(SampleSet) --> sample(Sample)
        audittrailentryset(AuditTrailEntrySet) --> audittrailentry(AuditTrailEntry)
        experimentstepset(ExperimentStepSet) --> experimentstep(ExperimentStep)
        experimentstepset(ExperimentStepSet) --> template(Template)
        sample(Sample) --> tagset(TagSet)
        sample(Sample) --> category(Category)
        audittrailentry(AuditTrailEntry) --> author(Author)
        audittrailentry(AuditTrailEntry) --> software(Software)
        audittrailentry(AuditTrailEntry) --> diff(Diff)
        template(Template) --> tagset(TagSet)
        template(Template) --> technique(Technique)
        template(Template) --> infrastructure(Infrastructure)
        template(Template) --> method(Method)
        template(Template) --> result(Result)
        experimentstep(ExperimentStep) --> tagset(TagSet)
        experimentstep(ExperimentStep) --> technique(Technique)
        experimentstep(ExperimentStep) --> infrastructure(Infrastructure)
        experimentstep(ExperimentStep) --> method(Method)
        experimentstep(ExperimentStep) --> result(Result)
        tagset(TagSet) --> tag(Tag)
        result(Result) --> seriesset(SeriesSet)
        result(Result) --> category(Category)
        method(Method) --> author(Author)
        method(Method) --> device(Device)
        method(Method) --> software(Software)
        method(Method) --> category(Category)
        technique(Technique) --> extension(Extension)
        infrastructure(Infrastructure) --> samplereferenceset(SampleReferenceSet)
        infrastructure(Infrastructure) --> parentdatapointreferenceset(ParentDataPointReferenceSet)
        infrastructure(Infrastructure) --> experimentdatareferenceset(ExperimentDataReferenceSet)
        category(Category) --> parameter(Parameter)
        category(Category) --> seriesset(SeriesSet)
        category(Category) --> category(Category)
        experimentdatareferenceset(ExperimentDataReferenceSet) --> experimentdatareference(ExperimentDataReference)
        experimentdatareferenceset(ExperimentDataReferenceSet) --> experimentdatabulkreference(ExperimentDataBulkReference)
        parentdatapointreferenceset(ParentDataPointReferenceSet) --> parentdatapointreference(ParentDataPointReference)
        samplereferenceset(SampleReferenceSet) --> samplereference(SampleReference)
        samplereferenceset(SampleReferenceSet) --> sampleinheritance(SampleInheritance)
        seriesset(SeriesSet) --> series(Series)
        parameter(Parameter) --> unit(Unit)
        parentdatapointreference(ParentDataPointReference) --> startvalue(StartValue)
        parentdatapointreference(ParentDataPointReference) --> endvalue(EndValue)
        series(Series) --> individualvalueset(IndividualValueSet)
        series(Series) --> encodedvalueset(EncodedValueSet)
        series(Series) --> autoincrementedvalueset(AutoIncrementedValueSet)
        series(Series) --> unit(Unit)
        unit(Unit) --> siunit(SIUnit)
        autoincrementedvalueset(AutoIncrementedValueSet) --> startvalue(StartValue)
        autoincrementedvalueset(AutoIncrementedValueSet) --> increment(Increment)

        click animl "#animl" "Go to AnIML"
        click sampleset "#sampleset" "Go to SampleSet"
        click audittrailentryset "#audittrailentryset" "Go to AuditTrailEntrySet"
        click experimentstepset "#experimentstepset" "Go to ExperimentStepSet"
        click sample "#sample" "Go to Sample"
        click audittrailentry "#audittrailentry" "Go to AuditTrailEntry"
        click template "#template" "Go to Template"
        click experimentstep "#experimentstep" "Go to ExperimentStep"
        click diff "#diff" "Go to Diff"
        click author "#author" "Go to Author"
        click software "#software" "Go to Software"
        click tagset "#tagset" "Go to TagSet"
        click result "#result" "Go to Result"
        click method "#method" "Go to Method"
        click technique "#technique" "Go to Technique"
        click infrastructure "#infrastructure" "Go to Infrastructure"
        click tag "#tag" "Go to Tag"
        click category "#category" "Go to Category"
        click device "#device" "Go to Device"
        click extension "#extension" "Go to Extension"
        click experimentdatareferenceset "#experimentdatareferenceset" "Go to ExperimentDataReferenceSet"
        click parentdatapointreferenceset "#parentdatapointreferenceset" "Go to ParentDataPointReferenceSet"
        click samplereferenceset "#samplereferenceset" "Go to SampleReferenceSet"
        click seriesset "#seriesset" "Go to SeriesSet"
        click parameter "#parameter" "Go to Parameter"
        click experimentdatareference "#experimentdatareference" "Go to ExperimentDataReference"
        click experimentdatabulkreference "#experimentdatabulkreference" "Go to ExperimentDataBulkReference"
        click parentdatapointreference "#parentdatapointreference" "Go to ParentDataPointReference"
        click samplereference "#samplereference" "Go to SampleReference"
        click sampleinheritance "#sampleinheritance" "Go to SampleInheritance"
        click series "#series" "Go to Series"
        click siunit "#siunit" "Go to SIUnit"
        click endvalue "#endvalue" "Go to EndValue"
        click individualvalueset "#individualvalueset" "Go to IndividualValueSet"
        click unit "#unit" "Go to Unit"
        click autoincrementedvalueset "#autoincrementedvalueset" "Go to AutoIncrementedValueSet"
        click encodedvalueset "#encodedvalueset" "Go to EncodedValueSet"
        click startvalue "#startvalue" "Go to StartValue"
        click increment "#increment" "Go to Increment"
    ```


## Types


### AnIML
ComplexType for the root element of an AnIML document. The AnIML element serves as the container for all data and metadata in an analytical data file. It contains version information, sample definitions, experimental data organized in steps, and an audit trail of changes made to the document.

__version__* `string`

- Version number of the AnIML Core Schema used in this document. Must be '0.90'.

- `Default`: 0.9

__sample_set__ [`SampleSet`](#sampleset)

- Container for Samples used in this AnIML document.


__experiment_step_set__ [`ExperimentStepSet`](#experimentstepset)

- Container for multiple ExperimentSteps that describe the process and results.


__audit_trail_entry_set__ [`AuditTrailEntrySet`](#audittrailentryset)

- Container for audit trail entries describing changes to this document.


------

### SampleSet
Container for Samples used in this AnIML document. The SampleSet element acts as a registry of all samples referenced throughout the document, allowing samples to be defined once and referenced multiple times. This centralized approach ensures consistency in sample identification and properties across the entire analytical workflow.

__sample__ [`list[Sample]`](#sample)

- Individual Sample, referenced from other parts of this AnIML document.


------

### AuditTrailEntrySet
Container for audit trail entries describing changes to this document. The AuditTrailEntrySet maintains a chronological record of all modifications made to the AnIML document, including who made the changes, when they were made, and what specific changes occurred. This provides full traceability and compliance with data integrity requirements.

__audit_trail_entry__ [`list[AuditTrailEntry]`](#audittrailentry)

- Describes a set of changes made to the particular AnIML document by one user at a given time.


------

### ExperimentStepSet
Container for multiple ExperimentSteps that describe the process and results. The ExperimentStepSet organizes the analytical workflow into discrete steps, where each step represents the application of a specific analytical technique. This structure allows for clear documentation of complex, multi-step analytical procedures while maintaining relationships between steps.

__experiment_step__ [`list[ExperimentStep]`](#experimentstep)

- Container that documents a step in an experiment. Use one ExperimentStep per application of a Technique.


__template__ [`list[Template]`](#template)

- Represents a template for an ExperimentStep.


------

### Sample
Individual Sample, referenced from other parts of this AnIML document. The Sample element provides comprehensive documentation of a physical or virtual sample, including its identification, physical location, containment hierarchy, and any relevant metadata. It supports both simple samples and complex container-based sample organizations like well plates.

__name__* `string`

- Plain-text name of this item.


__sample_id__* `string`

- None


__barcode__ `string`

- Value of barcode label that is attached to sample container.


__comment__ `string`

- Unstructured text comment to further describe the Sample.


__derived__ `string`

- Indicates whether this is a derived Sample. A derived Sample is a Sample that has been created by applying a Technique. (Sub-Sampling, Processing, ...)


__container_type__ `string`

- Whether this sample is also a container for other samples. Set to 'simple' if not.


__container_id__ `string`

- Sample ID of container in which this sample is located.


__location_in_container__ `string`

- Coordinates of this sample within the enclosing container. In case of microplates or trays, the row is identified by letters and the column is identified by numbers (1-based) while in landscape orientation. Examples: A10 = 1st row, 10th column, Z1 = 26th row, 1st column, AB2 = 28th row, 2nd column.


__source_data_location__ `string`

- Points to the original data source. May be a file name, uri, database ID, etc.


__tag_set__ [`TagSet`](#tagset)

- Set of Tag elements.


__category__ [`list[Category]`](#category)

- Defines a category of Parameters and SeriesSets. Used to model hierarchies.


------

### AuditTrailEntry
Describes a set of changes made to the particular AnIML document by one user at a given time. The AuditTrailEntry element captures the complete context of a document modification event, including who made the change, when it occurred, what software was used, and both human-readable and machine-readable descriptions of the changes. This enables full traceability of document history.

__timestamp__* `string`

- Date and time of modification.


__author__* [`Author`](#author)

- Information about a person, a device or a piece of software authoring AnIML files.


__action__* `string`

- Type of change made (created, modified, ...)


__software__ [`Software`](#software)

- Software used to author this.


__reason__ `string`

- Explanation why changes were made.


__comment__ `string`

- Human-readable comment further explaining the changes.


__diff__ [`list[Diff]`](#diff)

- Machine-readable description of changes made.


__reference__ `list[string]`

- ID of the SignableItem that was affected. If none is specified, entire document is covered.


------

### Template
Represents a template for an ExperimentStep.

__name__* `string`

- Plain-text name of this item.


__template_id__* `string`

- None


__source_data_location__ `string`

- Points to the original data source. May be a file name, uri, database ID, etc.


__tag_set__ [`TagSet`](#tagset)

- Set of Tag elements.


__technique__ [`Technique`](#technique)

- Reference to Technique Definition used in this Experiment.


__infrastructure__ [`Infrastructure`](#infrastructure)

- Contains references to the context of this Experiment.


__method__ [`Method`](#method)

- Describes how this Experiment was performed.


__result__ [`list[Result]`](#result)

- Container for Data derived from Experiment.


------

### ExperimentStep
Container that documents a step in an experiment. Use one ExperimentStep per application of a Technique.

__name__* `string`

- Plain-text name of this item.


__experiment_step_id__* `string`

- Unique identifier for this ExperimentStep. Used to point to this step from an ExperimentDataReference.


__template_used__ `string`

- None


__comment__ `string`

- Unstructured text comment to further describe the ExperimentStep.


__source_data_location__ `string`

- Points to the original data source. May be a file name, uri, database ID, etc.


__tag_set__ [`TagSet`](#tagset)

- Set of Tag elements.


__technique__ [`Technique`](#technique)

- Reference to Technique Definition used in this Experiment.


__infrastructure__ [`Infrastructure`](#infrastructure)

- Contains references to the context of this Experiment.


__method__ [`Method`](#method)

- Describes how this Experiment was performed.


__result__ [`list[Result]`](#result)

- Container for Data derived from Experiment.


------

### Diff
Machine-readable description of changes made.

__scope__* `string`

- Scope of diff. May be 'element' or 'attribute'.


__changed_item__* `string`

- ID of the SignableItem that was changed


__old_value__* `string`

- No descripiton provided


__new_value__* `string`

- No descripiton provided


------

### Author
Information about a person, a device or a piece of software authoring AnIML files.

__user_type__* `string`

- Type of user (human, device, software)


__name__* `string`

- Common name.


__affiliation__ `string`

- Organization the Author is affiliated with.


__role__ `string`

- Role the Author plays within the organization.


__email__ `string`

- RFC822-compliant email address.


__phone__ `string`

- Phone number.


__location__ `string`

- Location or physical address.


------

### Software
Software used to author this.

__name__* `string`

- Common name.


__manufacturer__ `string`

- Company name.


__version__ `string`

- Version identifier of software release.


__operating_system__ `string`

- Operating system the software was running on.


------

### TagSet
Set of Tag elements.

__tag__ [`list[Tag]`](#tag)

- Tag to mark related data items. When a value is given, it may also serve as a reference to an external data system.


------

### Result
Container for Data derived from Experiment.

__name__* `string`

- Plain-text name of this item.


__series_set__ [`SeriesSet`](#seriesset)

- Container for n-dimensional Data.


__category__ [`list[Category]`](#category)

- Defines a category of Parameters and SeriesSets. Used to model hierarchies.


------

### Method
Describes how this Experiment was performed.

__name__ `string`

- Optional method name, as defined in the instrument software.


__author__ [`Author`](#author)

- Information about a person, a device or a piece of software authoring AnIML files.


__device__ [`Device`](#device)

- Device used to perform experiment.


__software__ [`Software`](#software)

- Software used to author this.


__category__ [`list[Category]`](#category)

- Defines a category of Parameters and SeriesSets. Used to model hierarchies.


------

### Technique
Reference to Technique Definition used in this Experiment.

__name__* `string`

- Plain-text name of this item.


__uri__* `string`

- URI where Technique Definition file can be fetched.


__sha256__ `string`

- SHA256 checksum of the referenced Technique Definition. Hex encoded, lower cased. Similar to the output of the sha256 unix command.


__extension__ [`list[Extension]`](#extension)

- Reference to an Extension to amend the active Technique Definition.


------

### Infrastructure
Contains references to the context of this Experiment.

__sample_reference_set__ [`SampleReferenceSet`](#samplereferenceset)

- Set of Samples used in this Experiment.


__parent_data_point_reference_set__ [`ParentDataPointReferenceSet`](#parentdatapointreferenceset)

- Contains references to the parent Result.


__experiment_data_reference_set__ [`ExperimentDataReferenceSet`](#experimentdatareferenceset)

- Set of Experiment Steps consumed by this Experiment Step.


__timestamp__ `string`

- Date and time of modification.


------

### Tag
Tag to mark related data items. When a value is given, it may also serve as a reference to an external data system.

__name__* `string`

- None


__value__ `string`

- None


------

### Category
Defines a category of Parameters and SeriesSets. Used to model hierarchies.

__name__* `string`

- Plain-text name of this item.


__parameter__ [`list[Parameter]`](#parameter)

- Name/Value Pair.


__series_set__ [`list[SeriesSet]`](#seriesset)

- Container for n-dimensional Data.


__category__ [`list[Category]`](#category)

- Defines a category of Parameters and SeriesSets. Used to model hierarchies.


------

### Device
Device used to perform experiment.

__name__* `string`

- Common name.


__device_identifier__ `string`

- Unique name or identifier of the device.


__manufacturer__ `string`

- Company name.


__firmware_version__ `string`

- Version identifier of firmware release.


__serial_number__ `string`

- Unique serial number of device.


------

### Extension
Reference to an Extension to amend the active Technique Definition.

__uri__* `string`

- URI where Extension file can be fetched.


__name__* `string`

- Name of Extension to be used. Must match Name given in Extension Definition file.


__sha256__ `string`

- SHA256 checksum of the referenced Extension. Hex encoded, lower cased. Similar to the output of the sha256 unix command.


------

### ExperimentDataReferenceSet
Set of Experiment Steps consumed by this Experiment Step.

__experiment_data_reference__ [`list[ExperimentDataReference]`](#experimentdatareference)

- Reference to an Experiment Step whose data is consumed.


__experiment_data_bulk_reference__ [`list[ExperimentDataBulkReference]`](#experimentdatabulkreference)

- Prefix-based reference to a set of Experiment Steps whose data are consumed.


------

### ParentDataPointReferenceSet
Contains references to the parent Result.

__parent_data_point_reference__* [`list[ParentDataPointReference]`](#parentdatapointreference)

- Reference to a data point or value range in an independent Series in the parent Result.


------

### SampleReferenceSet
Set of Samples used in this Experiment.

__sample_reference__ [`list[SampleReference]`](#samplereference)

- Reference to a Sample used in this Experiment.


__sample_inheritance__ [`list[SampleInheritance]`](#sampleinheritance)

- Indicates that a Sample was inherited from the parent ExperimentStep.


------

### SeriesSet
Container for n-dimensional Data.

__name__* `string`

- Plain-text name of this item.


__length__* `string`

- Number of data points each Series contains.


__series__* [`list[Series]`](#series)

- Container for multiple Values.


------

### Parameter
Name/Value Pair.

__name__* `string`

- Plain-text name of this item.


__parameter_type__* `string`

- Data type of this parameter


__value__* `integer``float``string``boolean`

- I: Individual integer value (32 bits, signed). L: Individual long integer value (64 bits, signed). F: Individual 32-bit floating point value. D: Individual 64-bit floating point value. S: Individual string value. Boolean: Individual boolean value.


__unit__ [`Unit`](#unit)

- Unit: Definition of a Scientific Unit.


------

### ExperimentDataReference
Reference to an Experiment Step whose data is consumed.

__role__* `string`

- None


__data_purpose__* `string`

- None


__experiment_step_id__* `string`

- None


------

### ExperimentDataBulkReference
Prefix-based reference to a set of Experiment Steps whose data are consumed.

__role__* `string`

- None


__data_purpose__* `string`

- None


__experiment_step_id_prefix__* `string`

- None


------

### ParentDataPointReference
Reference to a data point or value range in an independent Series in the parent Result.

__series_id__* `string`

- Contains the ID of the Series referenced.


__start_value__* [`StartValue`](#startvalue)

- Lower boundary of an interval or ValueSet.


__end_value__ [`EndValue`](#endvalue)

- Upper boundary of an interval.


------

### SampleReference
Reference to a Sample used in this Experiment.

__sample_id__* `string`

- SampleID of the Sample used in the current ExperimentStep. Refers to the sampleID within the SampleSet section of the document.


__role__* `string`

- Role this sample plays within the current ExperimentStep.


__sample_purpose__* `string`

- Specifies whether the referenced sample is produced or consumed by the current ExperimentStep.


------

### SampleInheritance
Indicates that a Sample was inherited from the parent ExperimentStep.

__role__* `string`

- Role this sample plays within the current ExperimentStep.


__sample_purpose__* `string`

- Specifies whether the referenced sample is produced or consumed by the current ExperimentStep.


------

### Series
Container for multiple Values.

__name__* `string`

- Plain-text name of this item.


__dependency__* `string`

- Specified whether the Series is independent or dependent.


__series_id__* `string`

- Identifies the Series. Used in References from subordinate ExperimentSteps. Unique per SeriesSet.


__series_type__* `string`

- Data type used by all values in this Series.


__visible__ `string`

- Specifies whether data in this Series is to be displayed to the user by default.


__plot_scale__ `string`

- Specifies whether the data in this Series is typically plotted on a linear or logarithmic scale.


__value_set__ [`IndividualValueSet`](#individualvalueset)[`EncodedValueSet`](#encodedvalueset)[`AutoIncrementedValueSet`](#autoincrementedvalueset)

- IndividualValueSet: Multiple Values explicitly specified. EncodedValueSet: Multiple numeric values encoded as a base64 binary string. Uses little-endian byte order. AutoIncrementedValueSet: Multiple values given in form of a start value and an increment.


__unit__ [`Unit`](#unit)

- Definition of a Scientific Unit.


------

### SIUnit
Combination of SI Units used to represent Scientific unit

__factor__ `string`

- None


__exponent__ `string`

- None


__offset__ `string`

- None


------

### EndValue
Upper boundary of an interval.

__value__* `integer``float`

- I: Individual integer value (32 bits, signed). L: Individual long integer value (64 bits, signed). F: Individual 32-bit floating point value. D: Individual 64-bit floating point value.


------

### IndividualValueSet
Multiple Values explicitly specified.

__values__* `list[float]``list[integer]``list[string]``list[boolean]`

- I: Individual integer value (32 bits, signed). L: Individual long integer value (64 bits, signed). F: Individual 32-bit floating point value. D: Individual 64-bit floating point value. S: Individual string value. Boolean: Individual boolean value.


__start_index__ `string`

- Zero-based index of the first entry in this Value Set. The specification is inclusive.


__end_index__ `string`

- Zero-based index of the last entry in this Value Set. The specification is inclusive.


------

### Unit
Definition of a Scientific Unit.

__label__* `string`

- Defines the visual representation of a particular Unit.


__quantity__ `string`

- Quantity the unit can be applied to


__si_unit__ [`list[SIUnit]`](#siunit)

- Combination of SI Units used to represent Scientific unit


------

### AutoIncrementedValueSet
Multiple values given in form of a start value and an increment.

__start_value__* [`StartValue`](#startvalue)

- Lower boundary of an interval or ValueSet.


__increment__* [`Increment`](#increment)

- Increment value


__start_index__ `string`

- Zero-based index of the first entry in this Value Set. The specification is inclusive.


__end_index__ `string`

- Zero-based index of the last entry in this Value Set. The specification is inclusive.


------

### EncodedValueSet
Multiple numeric values encoded as a base64 binary string. Uses little-endian byte order.

__start_index__ `string`

- Zero-based index of the first entry in this Value Set. The specification is inclusive.


__end_index__ `string`

- Zero-based index of the last entry in this Value Set. The specification is inclusive.


------

### StartValue
Lower boundary of an interval or ValueSet.

__value__* `integer``float`

- I: Individual integer value (32 bits, signed). L: Individual long integer value (64 bits, signed). F: Individual 32-bit floating point value. D: Individual 64-bit floating point value.


------

### Increment
Increment value

__value__* `integer``float`

- I: Individual integer value (32 bits, signed). L: Individual long integer value (64 bits, signed). F: Individual 32-bit floating point value. D: Individual 64-bit floating point value.