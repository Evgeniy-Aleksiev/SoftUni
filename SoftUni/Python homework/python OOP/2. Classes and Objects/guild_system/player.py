class Player:
    default_guild_name = "Unaffiliated"

    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = Player.default_guild_name

    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills:
            return 'Skill already added'

        self.skills[skill_name] = mana_cost
        return f'Skill {skill_name} added to the collection of the player {self.name}'

    def player_info(self):
        result = f'Name: {self.name}\n' \
                 f'Guild: {self.guild}\n' \
                 f'HP: {self.hp}\n' \
                 f'MP: {self.mp}'

        for skill_name, skill_mana in self.skills.items():
            result += f'\n==={skill_name} - {skill_mana}'

        return result + '\n'
