import asyncio

from dotenv import load_dotenv
from gpt_researcher.utils.enum import ReportType

from gpt_researcher import GPTResearcher

load_dotenv()


async def main():
    """
    This is a sample script that shows how to run a research report.
    """
    # Query
    query = "Top 5 easiest recipes for a tasty and easy dinner"
    researcher = GPTResearcher(query=query, report_type=ReportType.ResearchReport.value)
    # Conduct research on the given query
    await researcher.conduct_research()
    # Write the report
    report = await researcher.write_report()

    return report


if __name__ == "__main__":
    print(asyncio.run(main()))
