from player.repository.player_repository_impl import PlayerRepositoryImpl

name = "Sanghoon Lee"
print(f"Hello {name}")

playerRepository = PlayerRepositoryImpl()
playerRepository.create()
playerRepository.create()

playerList = playerRepository.findAll()
print(f"playerList: {playerList}")

for player in playerList:
    print(f"player: {player}")

firstPlayer = playerRepository.findById(1)
print(f"firstPlayer: {firstPlayer}")
