import argparse
from .io import load_recipes, save_json
from .core import plan_menu

def main():
    p = argparse.ArgumentParser(prog="mealmaker")
    p.add_argument("--recipes", default="data/recipes.sample.json", help="Chemin vers le fichier de recettes JSON")
    p.add_argument("--days", type=int, default=7, help="Nombre de jours à planifier")
    p.add_argument("--min-vege", type=int, default=2, help="Nombre minimum de recettes végétariennes")
    p.add_argument("--min-fish", type=int, default=2, help="Nombre minimum de recettes à base de poisson")
    p.add_argument("--max-meat", type=int, default=3, help="Nombre maximum de recettes à base de viande")
    p.add_argument("--max-time", type=int, default=None, help="Temps de préparation maximum (en minutes)")
    p.add_argument("--avg-budget", type=float, default=None, help="Budget moyen par recette (en euros)")
    p.add_argument("--tolerance", type=float, default=0.2, help="Tolérance sur le budget moyen")
    p.add_argument("--seed", type=int, default=42, help="Graine aléatoire pour reproductibilité")
    p.add_argument("--output", default=None, help="Chemin pour sauvegarder le JSON généré")

    
    p.add_argument(
        "--exclude-ingredients",
        nargs="+",
        help="Liste d'ingrédients à exclure (ex: oeuf lait gluten)."
    )

    args = p.parse_args()

    recipes = load_recipes(args.recipes)
    result = plan_menu(
        recipes,
        days=args.days,
        min_vege=args.min_vege,
        min_fish=args.min_fish,
        max_meat=args.max_meat,
        max_time=args.max_time,
        avg_budget=args.avg_budget,
        tolerance=args.tolerance,
        seed=args.seed,
        exclude_ingredients=args.exclude_ingredients,  # ✅ Passage de l’argument ici
    )

    save_json(result, args.output)

if __name__ == "__main__":
    main()
