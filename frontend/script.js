function refreshDashboard() {

    const extracted =
        document.getElementById(
            "recordsExtracted"
        );

    const loaded =
        document.getElementById(
            "recordsLoaded"
        );

    const summary =
        document.getElementById(
            "recordSummary"
        );

    extracted.textContent = "4";

    loaded.textContent = "4";

    summary.textContent =
        "4 customers";

    alert(
        "Dashboard refreshed successfully!"
    );
}


function showPipelineInfo() {

    alert(
        "DataSync ETL Pipeline\n\n" +
        "Extract → Validate → Transform → Load\n\n" +
        "Source: Stripe API\n" +
        "Destination: SQLite Database"
    );
}