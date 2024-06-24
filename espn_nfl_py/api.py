import requests
from .endpoints import ENDPOINTS
from .exceptions import APIError

class ESPNAPI:
    def _get(self, url):
        response = requests.get(url)
        if response.status_code != 200:
            raise APIError(f"API request failed with status {response.status_code}")
        return response.json()

    def get_probabilities(self, event_id):
        return self._get(ENDPOINTS["ODDS"]["PROBABILITIES"](event_id))

    def get_odds(self, event_id):
        return self._get(ENDPOINTS["ODDS"]["ODDS"](event_id))

    def get_predictor(self, event_id):
        return self._get(ENDPOINTS["ODDS"]["PREDICTOR"](event_id))

    def get_ats(self, year, team_id):
        return self._get(ENDPOINTS["ODDS"]["ATS"](year, team_id))

    def get_futures(self, year):
        return self._get(ENDPOINTS["ODDS"]["FUTURES"](year))

    def get_h2h(self, event_id, bet_provider_id):
        return self._get(ENDPOINTS["ODDS"]["H2H"](event_id, bet_provider_id))

    def get_odds_records(self, year, team_id):
        return self._get(ENDPOINTS["ODDS"]["ODDS_RECORDS"](year, team_id))

    def get_game_odds(self, event_id, bet_provider_id):
        return self._get(ENDPOINTS["ODDS"]["GAME_ODDS"](event_id, bet_provider_id))

    def get_qbr(self, year, week_num):
        return self._get(ENDPOINTS["ODDS"]["QBR"](year, week_num))

    def get_past_performances(self, team_id, bet_provider_id):
        return self._get(ENDPOINTS["ODDS"]["PAST_PERFORMANCES"](team_id, bet_provider_id))

    def get_athletes(self, year, team_id):
        return self._get(ENDPOINTS["TEAMS"]["ATHLETES"](year, team_id))

    def get_team_events(self, year, team_id):
        return self._get(ENDPOINTS["TEAMS"]["EVENTS"](year, team_id))

    def get_teams(self):
        return self._get(ENDPOINTS["TEAMS"]["TEAMS"])

    def get_team(self, team_id):
        return self._get(ENDPOINTS["TEAMS"]["TEAM"](team_id))

    def get_season_teams(self, year):
        return self._get(ENDPOINTS["TEAMS"]["SEASON_TEAMS"](year))

    def get_season_team(self, year, team_id):
        return self._get(ENDPOINTS["TEAMS"]["SEASON_TEAM"](year, team_id))

    def get_season_leaders(self, year, season_type):
        return self._get(ENDPOINTS["TEAMS"]["SEASON_LEADERS"](year, season_type))

    def get_record(self, year, season_type, team_id):
        return self._get(ENDPOINTS["TEAMS"]["RECORD"](year, season_type, team_id))

    def get_depthcharts(self, year, team_id):
        return self._get(ENDPOINTS["TEAMS"]["DEPTHCHARTS"](year, team_id))

    def get_roster(self, team_id):
        return self._get(ENDPOINTS["TEAMS"]["ROSTER"](team_id))

    def get_detailed_roster(self, team_id):
        return self._get(ENDPOINTS["TEAMS"]["DETAILED_ROSTER"](team_id))

    def get_schedule(self, team_id, year):
        return self._get(ENDPOINTS["TEAMS"]["SCHEDULE"](team_id, year))

    def get_injuries(self, team_id):
        return self._get(ENDPOINTS["TEAMS"]["INJURIES"](team_id))

    def get_statistics(self, year, season_type, team_id):
        return self._get(ENDPOINTS["TEAMS"]["STATISTICS"](year, season_type, team_id))

    def get_projection(self, year, team_id):
        return self._get(ENDPOINTS["TEAMS"]["PROJECTION"](year, team_id))

    def get_season_standing(self, year, season_type, conference_id):
        return self._get(ENDPOINTS["TEAMS"]["SEASON_STANDING"](year, season_type, conference_id))

    def get_game_summary(self, event_id):
        return self._get(ENDPOINTS["GAMES"]["SUMMARY"](event_id))

    def get_play_by_play(self, event_id):
        return self._get(ENDPOINTS["GAMES"]["PLAY_BY_PLAY"](event_id))

    def get_linescores(self, event_id, team_id):
        return self._get(ENDPOINTS["GAMES"]["LINESCORES"](event_id, team_id))

    def get_scoring(self, event_id, team_id):
        return self._get(ENDPOINTS["GAMES"]["SCORING"](event_id, team_id))

    def get_game_roster(self, event_id, team_id):
        return self._get(ENDPOINTS["GAMES"]["ROSTER"](event_id, team_id))

    def get_talent_picks(self, year, season_type, week_num):
        return self._get(ENDPOINTS["GAMES"]["TALENT_PICKS"](year, season_type, week_num))

    def get_weekly_event_ids(self, year, season_type, week_num):
        return self._get(ENDPOINTS["GAMES"]["WEEKLY_EVENT_IDS"](year, season_type, week_num))

    def get_officials(self, event_id):
        return self._get(ENDPOINTS["GAMES"]["OFFICIALS"](event_id))

    def get_powerindex(self, event_id, team_id):
        return self._get(ENDPOINTS["GAMES"]["POWERINDEX"](event_id, team_id))

    def get_athlete_splits(self, athlete_id):
        return self._get(ENDPOINTS["ATHLETES"]["SPLITS"](athlete_id))

    def get_athletes_list(self):
        return self._get(ENDPOINTS["ATHLETES"]["ATHLETES"])

    def get_athlete_eventlog(self, year, athlete_id):
        return self._get(ENDPOINTS["ATHLETES"]["EVENTLOG"](year, athlete_id))

    def get_athlete_event_stats(self, event_id, team_id, athlete_id):
        return self._get(ENDPOINTS["ATHLETES"]["EVENT_STATS"](event_id, team_id, athlete_id))

    def get_leaders(self):
        return self._get(ENDPOINTS["ATHLETES"]["LEADERS"])

    def get_talent_picks_athlete(self):
        return self._get(ENDPOINTS["ATHLETES"]["TALENT_PICKS"])

    def get_athlete_gamelog(self, athlete_id):
        return self._get(ENDPOINTS["ATHLETES"]["GAMELOG"](athlete_id))

    def get_coaches(self, year):
        return self._get(ENDPOINTS["ATHLETES"]["COACHES"](year))

    def get_statistics_log(self, athlete_id):
        return self._get(ENDPOINTS["ATHLETES"]["STATISTICS_LOG"](athlete_id))

    def get_athlete_overview(self, athlete_id):
        return self._get(ENDPOINTS["ATHLETES"]["OVERVIEW"](athlete_id))

    def get_free_agents(self, year):
        return self._get(ENDPOINTS["ATHLETES"]["FREE_AGENTS"](year))

    def get_draft(self, year):
        return self._get(ENDPOINTS["ATHLETES"]["DRAFT"](year))

    def get_ondays(self):
        return self._get(ENDPOINTS["CALENDAR"]["ONDAYS"])

    def get_offdays(self):
        return self._get(ENDPOINTS["CALENDAR"]["OFFDAYS"])

    def get_blacklist(self):
        return self._get(ENDPOINTS["CALENDAR"]["BLACKLIST"])

    def get_whitelist(self):
        return self._get(ENDPOINTS["CALENDAR"]["WHITELIST"])

    def get_weeks(self, year, season_type):
        return self._get(ENDPOINTS["CALENDAR"]["WEEKS"](year, season_type))

    def get_week_info(self, year, season_type, week_num):
        return self._get(ENDPOINTS["CALENDAR"]["WEEK_INFO"](year, season_type, week_num))

    def get_season(self, year):
        return self._get(ENDPOINTS["CALENDAR"]["SEASON"](year))

    def get_transactions(self):
        return self._get(ENDPOINTS["SCOREBOARD"]["TRANSACTIONS"])

    def get_groups(self, year, season_type):
        return self._get(ENDPOINTS["SCOREBOARD"]["GROUPS"](year, season_type))

    def get_franchises(self):
        return self._get(ENDPOINTS["SCOREBOARD"]["FRANCHISES"])

    def get_header(self):
        return self._get(ENDPOINTS["SCOREBOARD"]["HEADER"])
