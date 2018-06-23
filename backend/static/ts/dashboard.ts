function trend_label(diff?: number): string {
    if (diff === undefined || diff === null) {
        return "";
    }
    if (diff < 3) {
        return "label-success";
    }
    if (diff < 4) {
        return "label-warning";
    }
    return "label-danger";
}