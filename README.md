# CSSDATA

CSSDATA is a comprehensive, structured dataset of CSS language features, including properties, at-rules, selectors, syntaxes, types, and units. It is designed to support tooling, validation, documentation, and analysis of CSS by providing machine-readable JSON files that describe the syntax and metadata of CSS features.

## Project Structure

- **data/**: Contains the main CSS data files.
  - **merged_raw_data.json**: All CSS data merged into a single file.
  - **individual_files/**: Separate JSON files for each CSS feature category.
- **schema/**: JSON Schema definitions for validating the data files.
  - **merged-schema.json**: Combined schema for all data.
  - **individual_files/**: Schemas for each feature category.
- **merged-all-unit_and_types_syntaxes_selectors_properties_functions_at_rules_schema.json**: A comprehensive merged schema/data file.

## Data Contents

Each data file describes CSS features with rich metadata, such as:
- **syntax**: The formal syntax of the feature.
- **media**: Applicable media types.
- **initial**: Initial value.
- **percentages**: How percentages are interpreted.
- **computed**: Computed value rules.
- **order**: Order of values or appearance.
- **status**: Standardization status (standard, nonstandard, experimental, obsolete).
- **mdn_url**: Link to MDN documentation.
- **groups**: Feature grouping/category.

## Use Cases

- **CSS linters and validators**
- **Editor and IDE autocompletion**
- **Documentation generation**
- **Static analysis and code intelligence**
- **Browser compatibility tools**

## Contributing

Contributions are welcome! Please open issues or pull requests for corrections, additions, or improvements to the data or schemas.

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

Data sources include the [MDN Web Docs](https://developer.mozilla.org/) and contributions from the CSS community.