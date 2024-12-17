import * as D from 'io-ts/Decoder';
import { isLeft } from "fp-ts/Either";

// Generic validate function
export function validate<T>(codec: D.Decoder<unknown, T>, value: unknown): T {
  const result = codec.decode(value);
  if (isLeft(result)) {
    throw new Error(D.draw(result.left));
  }
  return result.right;
}

// JSON-LD Types
export interface JsonLdContext {
  [key: string]: any;
}

export interface JsonLd {
  '@context'?: JsonLdContext;
  '@id'?: string;
  '@type'?: string;
}

// Analytical Information Markup Language Type definitions
/**
    ComplexType for the root element of an AnIML document. The AnIML
    element serves as the container for all data and metadata in an
    analytical data file. It contains version information, sample
    definitions, experimental data organized in steps, and an audit
    trail of changes made to the document.

    * @param version - Version number of the AnIML Core Schema used in this document. Must
             be '0.90'.
    * @param sample_set - Container for Samples used in this AnIML document.
    * @param experiment_step_set - Container for multiple ExperimentSteps that describe the process and
             results.
    * @param audit_trail_entry_set - Container for audit trail entries describing changes to this document.
**/
export interface AnIML extends JsonLd {
  version: string;
  sample_set?: SampleSet | null;
  experiment_step_set?: ExperimentStepSet | null;
  audit_trail_entry_set?: AuditTrailEntrySet | null;
}

export const AnIMLCodec = D.lazy("AnIML", () => D.struct({
    version: D.string,
    sample_set: D.nullable(SampleSetCodec),
    experiment_step_set: D.nullable(ExperimentStepSetCodec),
    audit_trail_entry_set: D.nullable(AuditTrailEntrySetCodec),
}));


/**
    Container for Samples used in this AnIML document. The SampleSet
    element acts as a registry of all samples referenced throughout
    the document, allowing samples to be defined once and referenced
    multiple times. This centralized approach ensures consistency in
    sample identification and properties across the entire analytical
    workflow.

    * @param sample - Individual Sample, referenced from other parts of this AnIML document.
**/
export interface SampleSet extends JsonLd {
  sample?: Sample[] | null;
}

export const SampleSetCodec = D.lazy("SampleSet", () => D.struct({
    sample: D.array(SampleCodec),
}));


/**
    Container for audit trail entries describing changes to this document.
    The AuditTrailEntrySet maintains a chronological record of all
    modifications made to the AnIML document, including who made the
    changes, when they were made, and what specific changes occurred.
    This provides full traceability and compliance with data integrity
    requirements.

    * @param audit_trail_entry - Describes a set of changes made to the particular AnIML document by
             one user at a given time.
**/
export interface AuditTrailEntrySet extends JsonLd {
  audit_trail_entry?: AuditTrailEntry[] | null;
}

export const AuditTrailEntrySetCodec = D.lazy("AuditTrailEntrySet", () => D.struct({
    audit_trail_entry: D.array(AuditTrailEntryCodec),
}));


/**
    Container for multiple ExperimentSteps that describe the process and
    results. The ExperimentStepSet organizes the analytical workflow
    into discrete steps, where each step represents the application of
    a specific analytical technique. This structure allows for clear
    documentation of complex, multi-step analytical procedures while
    maintaining relationships between steps.

    * @param experiment_step - Container that documents a step in an experiment. Use one
             ExperimentStep per application of a Technique.
    * @param template - Represents a template for an ExperimentStep.
**/
export interface ExperimentStepSet extends JsonLd {
  experiment_step?: ExperimentStep[] | null;
  template?: Template[] | null;
}

export const ExperimentStepSetCodec = D.lazy("ExperimentStepSet", () => D.struct({
    experiment_step: D.array(ExperimentStepCodec),
    template: D.array(TemplateCodec),
}));


/**
    Individual Sample, referenced from other parts of this AnIML document.
    The Sample element provides comprehensive documentation of a
    physical or virtual sample, including its identification, physical
    location, containment hierarchy, and any relevant metadata. It
    supports both simple samples and complex container-based sample
    organizations like well plates.

    * @param name - Plain-text name of this item.
    * @param sample_id - None
    * @param barcode - Value of barcode label that is attached to sample container.
    * @param comment - Unstructured text comment to further describe the Sample.
    * @param derived - Indicates whether this is a derived Sample. A derived Sample is a
             Sample that has been created by applying a Technique.
             (Sub-Sampling, Processing, ...)
    * @param container_type - Whether this sample is also a container for other samples. Set to
             'simple' if not.
    * @param container_id - Sample ID of container in which this sample is located.
    * @param location_in_container - Coordinates of this sample within the enclosing container. In case of
             microplates or trays, the row is identified by letters
             and the column is identified by numbers (1-based) while
             in landscape orientation. Examples: A10 = 1st row, 10th
             column, Z1 = 26th row, 1st column, AB2 = 28th row, 2nd
             column.
    * @param source_data_location - Points to the original data source. May be a file name, uri, database
             ID, etc.
    * @param tag_set - Set of Tag elements.
    * @param category - Defines a category of Parameters and SeriesSets. Used to model
             hierarchies.
**/
export interface Sample extends JsonLd {
  name: string;
  sample_id: string;
  barcode?: string | null;
  comment?: string | null;
  derived?: string | null;
  container_type?: string | null;
  container_id?: string | null;
  location_in_container?: string | null;
  source_data_location?: string | null;
  tag_set?: TagSet | null;
  category?: Category[] | null;
}

export const SampleCodec = D.lazy("Sample", () => D.struct({
    name: D.string,
    sample_id: D.string,
    barcode: D.nullable(D.string),
    comment: D.nullable(D.string),
    derived: D.nullable(D.string),
    container_type: D.nullable(D.string),
    container_id: D.nullable(D.string),
    location_in_container: D.nullable(D.string),
    source_data_location: D.nullable(D.string),
    tag_set: D.nullable(TagSetCodec),
    category: D.array(CategoryCodec),
}));


/**
    Describes a set of changes made to the particular AnIML document by
    one user at a given time. The AuditTrailEntry element captures
    the complete context of a document modification event, including
    who made the change, when it occurred, what software was used,
    and both human-readable and machine-readable descriptions of the
    changes. This enables full traceability of document history.

    * @param timestamp - Date and time of modification.
    * @param author - Information about a person, a device or a piece of software authoring
             AnIML files.
    * @param action - Type of change made (created, modified, ...)
    * @param software - Software used to author this.
    * @param reason - Explanation why changes were made.
    * @param comment - Human-readable comment further explaining the changes.
    * @param diff - Machine-readable description of changes made.
    * @param reference - ID of the SignableItem that was affected. If none is specified, entire
             document is covered.
**/
export interface AuditTrailEntry extends JsonLd {
  timestamp: string;
  author: Author;
  action: string;
  software?: Software | null;
  reason?: string | null;
  comment?: string | null;
  diff?: Diff[] | null;
  reference?: string[] | null;
}

export const AuditTrailEntryCodec = D.lazy("AuditTrailEntry", () => D.struct({
    timestamp: D.string,
    author: AuthorCodec,
    action: D.string,
    software: D.nullable(SoftwareCodec),
    reason: D.nullable(D.string),
    comment: D.nullable(D.string),
    diff: D.array(DiffCodec),
    reference: D.array(D.string),
}));


/**
    Represents a template for an ExperimentStep. Templates provide a
    reusable pattern for creating ExperimentSteps with predefined
    structure and metadata. They help ensure consistency across
    similar experimental procedures.

    * @param name - Plain-text name of this item.
    * @param template_id - None
    * @param source_data_location - Points to the original data source. May be a file name, uri, database
             ID, etc.
    * @param tag_set - Set of Tag elements.
    * @param technique - Reference to Technique Definition used in this Experiment.
    * @param infrastructure - Contains references to the context of this Experiment.
    * @param method - Describes how this Experiment was performed.
    * @param result - Container for Data derived from Experiment.
**/
export interface Template extends JsonLd {
  name: string;
  template_id: string;
  source_data_location?: string | null;
  tag_set?: TagSet | null;
  technique?: Technique | null;
  infrastructure?: Infrastructure | null;
  method?: Method | null;
  result?: Result[] | null;
}

export const TemplateCodec = D.lazy("Template", () => D.struct({
    name: D.string,
    template_id: D.string,
    source_data_location: D.nullable(D.string),
    tag_set: D.nullable(TagSetCodec),
    technique: D.nullable(TechniqueCodec),
    infrastructure: D.nullable(InfrastructureCodec),
    method: D.nullable(MethodCodec),
    result: D.array(ResultCodec),
}));


/**
    Container that documents a step in an experiment. Use one
    ExperimentStep per application of a Technique. ExperimentSteps are
    the fundamental building blocks of an AnIML document, capturing
    the complete context, method, and results of a single experimental
    procedure or measurement.

    * @param name - Plain-text name of this item.
    * @param experiment_step_id - Unique identifier for this ExperimentStep. Used to point to this step
             from an ExperimentDataReference.
    * @param template_used - None
    * @param comment - Unstructured text comment to further describe the ExperimentStep.
    * @param source_data_location - Points to the original data source. May be a file name, uri, database
             ID, etc.
    * @param tag_set - Set of Tag elements.
    * @param technique - Reference to Technique Definition used in this Experiment.
    * @param infrastructure - Contains references to the context of this Experiment.
    * @param method - Describes how this Experiment was performed.
    * @param result - Container for Data derived from Experiment.
**/
export interface ExperimentStep extends JsonLd {
  name: string;
  experiment_step_id: string;
  template_used?: string | null;
  comment?: string | null;
  source_data_location?: string | null;
  tag_set?: TagSet | null;
  technique?: Technique | null;
  infrastructure?: Infrastructure | null;
  method?: Method | null;
  result?: Result[] | null;
}

export const ExperimentStepCodec = D.lazy("ExperimentStep", () => D.struct({
    name: D.string,
    experiment_step_id: D.string,
    template_used: D.nullable(D.string),
    comment: D.nullable(D.string),
    source_data_location: D.nullable(D.string),
    tag_set: D.nullable(TagSetCodec),
    technique: D.nullable(TechniqueCodec),
    infrastructure: D.nullable(InfrastructureCodec),
    method: D.nullable(MethodCodec),
    result: D.array(ResultCodec),
}));


/**
    Machine-readable description of changes made. Diffs provide a detailed
    record of modifications made to an AnIML document, enabling
    precise tracking of what was changed, when, and by whom. This
    supports audit trails and change management requirements.

    * @param scope - Scope of diff. May be 'element' or 'attribute'.
    * @param changed_item - ID of the SignableItem that was changed
    * @param old_value - No descripiton provided
    * @param new_value - No descripiton provided
**/
export interface Diff extends JsonLd {
  scope: string;
  changed_item: string;
  old_value: string;
  new_value: string;
}

export const DiffCodec = D.lazy("Diff", () => D.struct({
    scope: D.string,
    changed_item: D.string,
    old_value: D.string,
    new_value: D.string,
}));


/**
    Information about a person, a device or a piece of software authoring
    AnIML files. Authors can be human users, automated systems, or
    software applications that create or modify AnIML documents. This
    flexible definition supports both manual and automated workflows
    while maintaining clear provenance.

    * @param user_type - Type of user (human, device, software)
    * @param name - Common name.
    * @param affiliation - Organization the Author is affiliated with.
    * @param role - Role the Author plays within the organization.
    * @param email - RFC822-compliant email address.
    * @param phone - Phone number.
    * @param location - Location or physical address.
**/
export interface Author extends JsonLd {
  user_type: string;
  name: string;
  affiliation?: string | null;
  role?: string | null;
  email?: string | null;
  phone?: string | null;
  location?: string | null;
}

export const AuthorCodec = D.lazy("Author", () => D.struct({
    user_type: D.string,
    name: D.string,
    affiliation: D.nullable(D.string),
    role: D.nullable(D.string),
    email: D.nullable(D.string),
    phone: D.nullable(D.string),
    location: D.nullable(D.string),
}));


/**
    Software used to author this. This element captures details about
    software applications involved in creating or modifying AnIML
    documents, including version information and operating environment
    details for reproducibility and troubleshooting.

    * @param name - Common name.
    * @param manufacturer - Company name.
    * @param version - Version identifier of software release.
    * @param operating_system - Operating system the software was running on.
**/
export interface Software extends JsonLd {
  name: string;
  manufacturer?: string | null;
  version?: string | null;
  operating_system?: string | null;
}

export const SoftwareCodec = D.lazy("Software", () => D.struct({
    name: D.string,
    manufacturer: D.nullable(D.string),
    version: D.nullable(D.string),
    operating_system: D.nullable(D.string),
}));


/**
    Set of Tag elements. TagSets provide a flexible mechanism for adding
    metadata and classifications to AnIML elements. They can be used
    to group related items, add external references, or implement
    custom categorization schemes.

    * @param tag - Tag to mark related data items. When a value is given, it may also
             serve as a reference to an external data system.
**/
export interface TagSet extends JsonLd {
  tag?: Tag[] | null;
}

export const TagSetCodec = D.lazy("TagSet", () => D.struct({
    tag: D.array(TagCodec),
}));


/**
    Container for Data derived from Experiment. Results store the
    actual experimental data along with its organization into
    series and categories. This structured approach allows for
    clear representation of both simple and complex multidimensional
    datasets.

    * @param name - Plain-text name of this item.
    * @param series_set - Container for n-dimensional Data.
    * @param category - Defines a category of Parameters and SeriesSets. Used to model
             hierarchies.
**/
export interface Result extends JsonLd {
  name: string;
  series_set?: SeriesSet | null;
  category?: Category[] | null;
}

export const ResultCodec = D.lazy("Result", () => D.struct({
    name: D.string,
    series_set: D.nullable(SeriesSetCodec),
    category: D.array(CategoryCodec),
}));


/**
    Describes how this Experiment was performed. Methods document the
    complete experimental procedure, including the people involved,
    equipment used, and software settings. This comprehensive record
    ensures experiments can be understood and potentially reproduced.

    * @param name - Optional method name, as defined in the instrument software.
    * @param author - Information about a person, a device or a piece of software authoring
             AnIML files.
    * @param device - Device used to perform experiment.
    * @param software - Software used to author this.
    * @param category - Defines a category of Parameters and SeriesSets. Used to model
             hierarchies.
**/
export interface Method extends JsonLd {
  name?: string | null;
  author?: Author | null;
  device?: Device | null;
  software?: Software | null;
  category?: Category[] | null;
}

export const MethodCodec = D.lazy("Method", () => D.struct({
    name: D.nullable(D.string),
    author: D.nullable(AuthorCodec),
    device: D.nullable(DeviceCodec),
    software: D.nullable(SoftwareCodec),
    category: D.array(CategoryCodec),
}));


/**
    Reference to Technique Definition used in this Experiment. Techniques
    define the standardized structure and vocabulary for specific
    types of experimental procedures. This reference system ensures
    consistent data organization across different implementations of
    the same technique.

    * @param name - Plain-text name of this item.
    * @param uri - URI where Technique Definition file can be fetched.
    * @param sha256 - SHA256 checksum of the referenced Technique Definition. Hex encoded,
             lower cased. Similar to the output of the sha256 unix
             command.
    * @param extension - Reference to an Extension to amend the active Technique Definition.
**/
export interface Technique extends JsonLd {
  name: string;
  uri: string;
  sha256?: string | null;
  extension?: Extension[] | null;
}

export const TechniqueCodec = D.lazy("Technique", () => D.struct({
    name: D.string,
    uri: D.string,
    sha256: D.nullable(D.string),
    extension: D.array(ExtensionCodec),
}));


/**
    Contains references to the context of this Experiment. Infrastructure
    elements provide the broader experimental context by linking
    to samples, related experiments, and temporal information. This
    creates a web of relationships between different experimental
    components.

    * @param sample_reference_set - Set of Samples used in this Experiment.
    * @param parent_data_point_reference_set - Contains references to the parent Result.
    * @param experiment_data_reference_set - Set of Experiment Steps consumed by this Experiment Step.
    * @param timestamp - Date and time of modification.
**/
export interface Infrastructure extends JsonLd {
  sample_reference_set?: SampleReferenceSet | null;
  parent_data_point_reference_set?: ParentDataPointReferenceSet | null;
  experiment_data_reference_set?: ExperimentDataReferenceSet | null;
  timestamp?: string | null;
}

export const InfrastructureCodec = D.lazy("Infrastructure", () => D.struct({
    sample_reference_set: D.nullable(SampleReferenceSetCodec),
    parent_data_point_reference_set: D.nullable(ParentDataPointReferenceSetCodec),
    experiment_data_reference_set: D.nullable(ExperimentDataReferenceSetCodec),
    timestamp: D.nullable(D.string),
}));


/**
    Tag to mark related data items. When a value is given, it may also
    serve as a reference to an external data system. Tags provide
    a flexible way to add metadata, create groupings, or link to
    external systems while maintaining the structured nature of AnIML
    documents.

    * @param name - None
    * @param value - None
**/
export interface Tag extends JsonLd {
  name: string;
  value?: string | null;
}

export const TagCodec = D.lazy("Tag", () => D.struct({
    name: D.string,
    value: D.nullable(D.string),
}));


/**
    Defines a category of Parameters and SeriesSets. Used to model
    hierarchies. Categories enable logical grouping and organization
    of experimental data and parameters, supporting complex data
    structures while maintaining clear relationships between elements.

    * @param name - Plain-text name of this item.
    * @param parameter - Name/Value Pair.
    * @param series_set - Container for n-dimensional Data.
    * @param category - Defines a category of Parameters and SeriesSets. Used to model
             hierarchies.
**/
export interface Category extends JsonLd {
  name: string;
  parameter?: Parameter[] | null;
  series_set?: SeriesSet[] | null;
  category?: Category[] | null;
}

export const CategoryCodec = D.lazy("Category", () => D.struct({
    name: D.string,
    parameter: D.array(ParameterCodec),
    series_set: D.array(SeriesSetCodec),
    category: D.array(CategoryCodec),
}));


/**
    Device used to perform experiment. This element captures detailed
    information about laboratory instruments and equipment used
    in experiments, supporting traceability and reproducibility
    requirements.

    * @param name - Common name.
    * @param device_identifier - Unique name or identifier of the device.
    * @param manufacturer - Company name.
    * @param firmware_version - Version identifier of firmware release.
    * @param serial_number - Unique serial number of device.
**/
export interface Device extends JsonLd {
  name: string;
  device_identifier?: string | null;
  manufacturer?: string | null;
  firmware_version?: string | null;
  serial_number?: string | null;
}

export const DeviceCodec = D.lazy("Device", () => D.struct({
    name: D.string,
    device_identifier: D.nullable(D.string),
    manufacturer: D.nullable(D.string),
    firmware_version: D.nullable(D.string),
    serial_number: D.nullable(D.string),
}));


/**
    Reference to an Extension to amend the active Technique Definition.
    Extensions allow for customization and enhancement of standard
    Technique Definitions while maintaining compatibility with the
    base specification.

    * @param uri - URI where Extension file can be fetched.
    * @param name - Name of Extension to be used. Must match Name given in Extension
             Definition file.
    * @param sha256 - SHA256 checksum of the referenced Extension. Hex encoded, lower cased.
             Similar to the output of the sha256 unix command.
**/
export interface Extension extends JsonLd {
  uri: string;
  name: string;
  sha256?: string | null;
}

export const ExtensionCodec = D.lazy("Extension", () => D.struct({
    uri: D.string,
    name: D.string,
    sha256: D.nullable(D.string),
}));


/**
    Set of Experiment Steps consumed by this Experiment Step. This
    element manages dependencies between different experimental
    steps, allowing for complex workflows where the output of one step
    becomes input for another.

    * @param experiment_data_reference - Reference to an Experiment Step whose data is consumed.
    * @param experiment_data_bulk_reference - Prefix-based reference to a set of Experiment Steps whose data are
             consumed.
**/
export interface ExperimentDataReferenceSet extends JsonLd {
  experiment_data_reference?: ExperimentDataReference[] | null;
  experiment_data_bulk_reference?: ExperimentDataBulkReference[] | null;
}

export const ExperimentDataReferenceSetCodec = D.lazy("ExperimentDataReferenceSet", () => D.struct({
    experiment_data_reference: D.array(ExperimentDataReferenceCodec),
    experiment_data_bulk_reference: D.array(ExperimentDataBulkReferenceCodec),
}));


/**
    Contains references to the parent Result. This element enables precise
    linking between related data points across different experimental
    steps, supporting detailed tracking of data relationships and
    dependencies.

    * @param parent_data_point_reference - Reference to a data point or value range in an independent Series in
             the parent Result.
**/
export interface ParentDataPointReferenceSet extends JsonLd {
  parent_data_point_reference: ParentDataPointReference[];
}

export const ParentDataPointReferenceSetCodec = D.lazy("ParentDataPointReferenceSet", () => D.struct({
    parent_data_point_reference: D.array(ParentDataPointReferenceCodec),
}));


/**
    Set of Samples used in this Experiment. This element manages
    relationships between experiments and samples, tracking both
    sample usage and sample transformations throughout experimental
    workflows.

    * @param sample_reference - Reference to a Sample used in this Experiment.
    * @param sample_inheritance - Indicates that a Sample was inherited from the parent ExperimentStep.
**/
export interface SampleReferenceSet extends JsonLd {
  sample_reference?: SampleReference[] | null;
  sample_inheritance?: SampleInheritance[] | null;
}

export const SampleReferenceSetCodec = D.lazy("SampleReferenceSet", () => D.struct({
    sample_reference: D.array(SampleReferenceCodec),
    sample_inheritance: D.array(SampleInheritanceCodec),
}));


/**
    Container for n-dimensional Data. SeriesSets organize related data
    series into logical groups, supporting both simple linear data
    and complex multi-dimensional datasets while maintaining clear
    relationships between dependent and independent variables.

    * @param name - Plain-text name of this item.
    * @param length - Number of data points each Series contains.
    * @param series - Container for multiple Values.
**/
export interface SeriesSet extends JsonLd {
  name: string;
  length: string;
  series: Series[];
}

export const SeriesSetCodec = D.lazy("SeriesSet", () => D.struct({
    name: D.string,
    length: D.string,
    series: D.array(SeriesCodec),
}));


/**
    Name/Value Pair. Parameters store individual data points and
    experimental settings, supporting multiple data types and optional
    units for complete scientific documentation.

    * @param name - Plain-text name of this item.
    * @param parameter_type - Data type of this parameter
    * @param value - I: Individual integer value (32 bits, signed). L: Individual long
             integer value (64 bits, signed). F: Individual 32-bit
             floating point value. D: Individual 64-bit floating point
             value. S: Individual string value. Boolean: Individual
             boolean value.
    * @param unit - Unit: Definition of a Scientific Unit.
**/
export interface Parameter extends JsonLd {
  name: string;
  parameter_type: string;
  value: number;
  unit?: Unit | null;
}

export const ParameterCodec = D.lazy("Parameter", () => D.struct({
    name: D.string,
    parameter_type: D.string,
    value: D.number,
    unit: D.nullable(UnitCodec),
}));


/**
    Reference to an Experiment Step whose data is consumed. This element
    creates explicit links between experimental steps, documenting how
    data flows through multi-step experimental procedures.

    * @param role - None
    * @param data_purpose - None
    * @param experiment_step_id - None
**/
export interface ExperimentDataReference extends JsonLd {
  role: string;
  data_purpose: string;
  experiment_step_id: string;
}

export const ExperimentDataReferenceCodec = D.lazy("ExperimentDataReference", () => D.struct({
    role: D.string,
    data_purpose: D.string,
    experiment_step_id: D.string,
}));


/**
    Prefix-based reference to a set of Experiment Steps whose data are
    consumed. This element enables efficient referencing of multiple
    related experimental steps through pattern matching.

    * @param role - None
    * @param data_purpose - None
    * @param experiment_step_id_prefix - None
**/
export interface ExperimentDataBulkReference extends JsonLd {
  role: string;
  data_purpose: string;
  experiment_step_id_prefix: string;
}

export const ExperimentDataBulkReferenceCodec = D.lazy("ExperimentDataBulkReference", () => D.struct({
    role: D.string,
    data_purpose: D.string,
    experiment_step_id_prefix: D.string,
}));


/**
    Reference to a data point or value range in an independent Series in
    the parent Result. This element enables precise linking between
    specific data points across different experimental steps.

    * @param series_id - Contains the ID of the Series referenced.
    * @param start_value - Lower boundary of an interval or ValueSet.
    * @param end_value - Upper boundary of an interval.
**/
export interface ParentDataPointReference extends JsonLd {
  series_id: string;
  start_value: StartValue;
  end_value?: EndValue | null;
}

export const ParentDataPointReferenceCodec = D.lazy("ParentDataPointReference", () => D.struct({
    series_id: D.string,
    start_value: StartValueCodec,
    end_value: D.nullable(EndValueCodec),
}));


/**
    Reference to a Sample used in this Experiment. This element creates
    explicit links between experiments and samples, documenting how
    samples are used or transformed during experimental procedures.

    * @param sample_id - SampleID of the Sample used in the current ExperimentStep. Refers
             to the sampleID within the SampleSet section of the
             document.
    * @param role - Role this sample plays within the current ExperimentStep.
    * @param sample_purpose - Specifies whether the referenced sample is produced or consumed by the
             current ExperimentStep.
**/
export interface SampleReference extends JsonLd {
  sample_id: string;
  role: string;
  sample_purpose: string;
}

export const SampleReferenceCodec = D.lazy("SampleReference", () => D.struct({
    sample_id: D.string,
    role: D.string,
    sample_purpose: D.string,
}));


/**
    Indicates that a Sample was inherited from the parent ExperimentStep.
    This element supports tracking sample lineage through multi-step
    experimental procedures.

    * @param role - Role this sample plays within the current ExperimentStep.
    * @param sample_purpose - Specifies whether the referenced sample is produced or consumed by the
             current ExperimentStep.
**/
export interface SampleInheritance extends JsonLd {
  role: string;
  sample_purpose: string;
}

export const SampleInheritanceCodec = D.lazy("SampleInheritance", () => D.struct({
    role: D.string,
    sample_purpose: D.string,
}));


/**
    Container for multiple Values. Series elements store ordered
    collections of data points, supporting multiple data types and
    optional units while maintaining relationships between dependent
    and independent variables.

    * @param name - Plain-text name of this item.
    * @param dependency - Specified whether the Series is independent or dependent.
    * @param series_id - Identifies the Series. Used in References from subordinate
             ExperimentSteps. Unique per SeriesSet.
    * @param series_type - Data type used by all values in this Series.
    * @param visible - Specifies whether data in this Series is to be displayed to the user
             by default.
    * @param plot_scale - Specifies whether the data in this Series is typically plotted on a
             linear or logarithmic scale.
    * @param value_set - IndividualValueSet: Multiple Values explicitly specified.
             EncodedValueSet: Multiple numeric values encoded as a
             base64 binary string. Uses little-endian byte order.
             AutoIncrementedValueSet: Multiple values given in form of
             a start value and an increment.
    * @param unit - Definition of a Scientific Unit.
**/
export interface Series extends JsonLd {
  name: string;
  dependency: string;
  series_id: string;
  series_type: string;
  visible?: string | null;
  plot_scale?: string | null;
  value_set?: IndividualValueSet | null;
  unit?: Unit | null;
}

export const SeriesCodec = D.lazy("Series", () => D.struct({
    name: D.string,
    dependency: D.string,
    series_id: D.string,
    series_type: D.string,
    visible: D.nullable(D.string),
    plot_scale: D.nullable(D.string),
    value_set: D.nullable(IndividualValueSetCodec),
    unit: D.nullable(UnitCodec),
}));


/**
    Combination of SI Units used to represent Scientific unit. This
    element enables precise specification of complex scientific units
    through combinations of base SI units.

    * @param factor - None
    * @param exponent - None
    * @param offset - None
**/
export interface SIUnit extends JsonLd {
  factor?: string | null;
  exponent?: string | null;
  offset?: string | null;
}

export const SIUnitCodec = D.lazy("SIUnit", () => D.struct({
    factor: D.nullable(D.string),
    exponent: D.nullable(D.string),
    offset: D.nullable(D.string),
}));


/**
    Upper boundary of an interval. This element works with StartValue to
    define precise numeric ranges for data selection and reference.

    * @param value - I: Individual integer value (32 bits, signed). L: Individual long
             integer value (64 bits, signed). F: Individual 32-bit
             floating point value. D: Individual 64-bit floating point
             value.
**/
export interface EndValue extends JsonLd {
  value: number;
}

export const EndValueCodec = D.lazy("EndValue", () => D.struct({
    value: D.number,
}));


/**
    Multiple Values explicitly specified. This element provides direct
    storage of data values, supporting multiple data types for maximum
    flexibility.

    * @param values - I: Individual integer value (32 bits, signed). L: Individual long
             integer value (64 bits, signed). F: Individual 32-bit
             floating point value. D: Individual 64-bit floating point
             value. S: Individual string value. Boolean: Individual
             boolean value.
    * @param start_index - Zero-based index of the first entry in this Value Set. The
             specification is inclusive.
    * @param end_index - Zero-based index of the last entry in this Value Set. The
             specification is inclusive.
**/
export interface IndividualValueSet extends JsonLd {
  values: number[];
  start_index?: string | null;
  end_index?: string | null;
}

export const IndividualValueSetCodec = D.lazy("IndividualValueSet", () => D.struct({
    values: D.array(D.number),
    start_index: D.nullable(D.string),
    end_index: D.nullable(D.string),
}));


/**
    Definition of a Scientific Unit. This element provides a structured
    way to specify scientific units, supporting both simple units and
    complex combinations of SI units.

    * @param label - Defines the visual representation of a particular Unit.
    * @param quantity - Quantity the unit can be applied to
    * @param si_unit - Combination of SI Units used to represent Scientific unit
**/
export interface Unit extends JsonLd {
  label: string;
  quantity?: string | null;
  si_unit?: SIUnit[] | null;
}

export const UnitCodec = D.lazy("Unit", () => D.struct({
    label: D.string,
    quantity: D.nullable(D.string),
    si_unit: D.array(SIUnitCodec),
}));


/**
    Multiple values given in form of a start value and an increment. This
    element provides an efficient way to represent regular sequences
    of numeric values without storing each individual value.

    * @param start_value - Lower boundary of an interval or ValueSet.
    * @param increment - Increment value
    * @param start_index - Zero-based index of the first entry in this Value Set. The
             specification is inclusive.
    * @param end_index - Zero-based index of the last entry in this Value Set. The
             specification is inclusive.
**/
export interface AutoIncrementedValueSet extends JsonLd {
  start_value: StartValue;
  increment: Increment;
  start_index?: string | null;
  end_index?: string | null;
}

export const AutoIncrementedValueSetCodec = D.lazy("AutoIncrementedValueSet", () => D.struct({
    start_value: StartValueCodec,
    increment: IncrementCodec,
    start_index: D.nullable(D.string),
    end_index: D.nullable(D.string),
}));


/**
    Multiple numeric values encoded as a base64 binary string. Uses
    little-endian byte order. This element provides efficient storage
    of large numeric datasets through binary encoding.

    * @param start_index - Zero-based index of the first entry in this Value Set. The
             specification is inclusive.
    * @param end_index - Zero-based index of the last entry in this Value Set. The
             specification is inclusive.
**/
export interface EncodedValueSet extends JsonLd {
  start_index?: string | null;
  end_index?: string | null;
}

export const EncodedValueSetCodec = D.lazy("EncodedValueSet", () => D.struct({
    start_index: D.nullable(D.string),
    end_index: D.nullable(D.string),
}));


/**
    Lower boundary of an interval or ValueSet. This element works with
    EndValue to define precise numeric ranges for data selection and
    reference.

    * @param value - I: Individual integer value (32 bits, signed). L: Individual long
             integer value (64 bits, signed). F: Individual 32-bit
             floating point value. D: Individual 64-bit floating point
             value.
**/
export interface StartValue extends JsonLd {
  value: number;
}

export const StartValueCodec = D.lazy("StartValue", () => D.struct({
    value: D.number,
}));


/**
    Increment value. This element specifies the step size for
    AutoIncrementedValueSets, enabling efficient representation of
    regular numeric sequences.

    * @param value - I: Individual integer value (32 bits, signed). L: Individual long
             integer value (64 bits, signed). F: Individual 32-bit
             floating point value. D: Individual 64-bit floating point
             value.
**/
export interface Increment extends JsonLd {
  value: number;
}

export const IncrementCodec = D.lazy("Increment", () => D.struct({
    value: D.number,
}));