from brownie import AdvancedCollectible

def main():
    advancedCollectible = AdvancedCollectible[-1]
    num_of_advanced_collectibles = AdvancedCollectible.tokenCounter()
    print(f"You have {num_of_advanced_collectibles} collectibles")
    for token_id in range(num_of_advanced_collectibles):
        breed = advancedCollectible.tokenIdToBreed(token_id)
