from nextcord.ext import commands
import random

client = commands.Bot(command_prefix='!')
client.remove_command("help")

@client.command()
async def joke(ctx):
        await ctx.send(random.choice(
     [
    "pracowników należy traktować jak pieczarki: - trzymać w ciemnym pomieszczeniu, - od czasu do czasu obrzucić gównem, - jak któryś wystawi łeb - uciąć!",
    "Przychodzi pracownik do dyrektora: - Jestem zmuszony prosić pana o podwyżkę, ponieważ interesują się mną trzy firmy. - A mogę wiedzieć jakie to firmy? - pyta dyrektor. - Elektrownia, gazownia i wodociągi miejskie.",
    "-Jak pan myśli, co jest w dzisiejszych czasach większym problemem: niewiedza czy obojętność?, Nie wiem. Nie obchodzi mnie to.",
    "Najpopularniejszy zwrot w Czechach?, Cieszę się, że cię widzę!"
    ]
    ))
client.run("token")