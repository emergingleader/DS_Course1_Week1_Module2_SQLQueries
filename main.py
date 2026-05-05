import sqlite3
import pandas as pd

# ── Connections ──────────────────────────────────────────────────────────
conn1 = sqlite3.connect('planets.db')
conn2 = sqlite3.connect('dogs.db')
conn3 = sqlite3.connect('babe_ruth.db')


# ── Part 1: Basic Filtering (planets) ────────────────────────────────────

def get_no_moons():
    """Return all columns for planets that have 0 moons."""
    df_no_moons = pd.read_sql("""
SELECT * FROM planets
WHERE num_of_moons = 0
""", conn1)
    return df_no_moons


def get_name_seven():
    """Return name and mass of planets whose name is exactly 7 letters."""
    df_name_seven = pd.read_sql("""
SELECT name, mass FROM planets
WHERE LENGTH(name) = 7
""", conn1)
    return df_name_seven


# ── Part 2: Advanced Filtering (planets) ─────────────────────────────────

def get_mass():
    """Return name and mass of planets with mass <= 1.00."""
    df_mass = pd.read_sql("""
SELECT name, mass FROM planets
WHERE mass <= 1.00
""", conn1)
    return df_mass


def get_mass_moon():
    """Return all columns for planets with at least one moon and mass < 1.00."""
    df_mass_moon = pd.read_sql("""
SELECT * FROM planets
WHERE num_of_moons >= 1 AND mass < 1.00
""", conn1)
    return df_mass_moon


def get_blue():
    """Return name and color of planets whose color contains 'blue'."""
    df_blue = pd.read_sql("""
SELECT name, color FROM planets
WHERE color LIKE '%blue%'
""", conn1)
    return df_blue


# ── Part 3: Ordering and Limiting (dogs) ─────────────────────────────────

def get_hungry():
    """Return name, age, breed of hungry dogs sorted youngest to oldest."""
    df_hungry = pd.read_sql("""
SELECT name, age, breed FROM dogs
WHERE hungry = 1
ORDER BY age ASC
""", conn2)
    return df_hungry


def get_hungry_ages():
    """Return name, age, hungry for hungry dogs aged 2-7, sorted alphabetically."""
    df_hungry_ages = pd.read_sql("""
SELECT name, age, hungry FROM dogs
WHERE hungry = 1 AND age BETWEEN 2 AND 7
ORDER BY name ASC
""", conn2)
    return df_hungry_ages


def get_4_oldest():
    """Return name, age, breed for the 4 oldest dogs sorted alphabetically by breed."""
    df_4_oldest = pd.read_sql("""
SELECT name, age, breed FROM (
    SELECT name, age, breed FROM dogs
    ORDER BY age DESC
    LIMIT 4
)
ORDER BY breed ASC
""", conn2)
    return df_4_oldest


# ── Part 4: Aggregation (babe_ruth) ──────────────────────────────────────

def get_ruth_years():
    """Return the total number of years Babe Ruth played professional baseball."""
    df_ruth_years = pd.read_sql("""
SELECT COUNT(year) AS total_years
FROM babe_ruth_stats
""", conn3)
    return df_ruth_years


def get_hr_total():
    """Return the total number of home runs hit by Babe Ruth."""
    df_hr_total = pd.read_sql("""
SELECT SUM(HR) AS total_hr
FROM babe_ruth_stats
""", conn3)
    return df_hr_total


# ── Part 5: Grouping and Aggregation (babe_ruth) ──────────────────────────

def get_teams_years():
    """Return each team and the number of years Babe Ruth played for them."""
    df_teams_years = pd.read_sql("""
SELECT team, COUNT(year) AS number_years
FROM babe_ruth_stats
GROUP BY team
""", conn3)
    return df_teams_years


def get_at_bats():
    """Return teams where Babe Ruth averaged over 200 at bats, with the average."""
    df_at_bats = pd.read_sql("""
SELECT team, AVG(at_bats) AS average_at_bats
FROM babe_ruth_stats
GROUP BY team
HAVING AVG(at_bats) > 200
""", conn3)
    return df_at_bats
