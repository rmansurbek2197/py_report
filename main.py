class ReportGenerator:
    def generate(self, *data, **options):
        title = options.get("title", "Report")
        sort = options.get("sort", False)
        reverse = options.get("reverse", False)

        result = list(data)

        if sort:
            result = sorted(result, reverse=reverse)

        return {
            "title": title,
            "count": len(result),
            "data": result
        }


report = ReportGenerator()

print(report.generate(
    5, 2, 9, 1, 7,
    title="Sales Report",
    sort=True,
    reverse=True
))
