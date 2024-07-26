import duckdb
from loguru import logger

pl_duck = duckdb.connect('data/pl.duck.db')

pl_duck.sql("INSTALL httpfs")
pl_duck.sql("LOAD httpfs")

allowed = False

logger.info("Load duckdb table")

ctas = """
    CREATE OR REPLACE TABLE pl_standings_2023_2024 AS (
    SELECT
        column00 as pos,
        column01 as team_name,
        Home::INTEGER as home_matches,
        column03::INTEGER as home_wins,
        column04::INTEGER as home_draws,
        column05::INTEGER as home_losses,
        Away::INTEGER as away_matches,
        column07::INTEGER as away_wins,
        column08::INTEGER as away_draws,
        column09::INTEGER as away_losses,
        Total::INTEGER as matches,
        column11::INTEGER as wins,
        column12::INTEGER as draws,
        column13::INTEGER as losses,
        column14::INTEGER as favor_goals,
        column15::INTEGER as against_goals,
        column16::INTEGER as difference,
        column17::INTEGER as points
    FROM(
        SELECT * FROM read_csv('data/2023_2024_pl_standings.csv') OFFSET 1)
    );
"""

pl_duck.execute(ctas)

logger.info("Done!")