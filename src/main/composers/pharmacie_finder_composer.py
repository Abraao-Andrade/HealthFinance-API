from src.infra.db.repositories.pharmacies_repository import PharmaciesRepository
from src.data.use_cases.pharmacies_finder import PharmacieFinder
from src.presentation.controllers.pharmacie_finder_controller import PharmacieFinderController


def pharmacie_finder_composer():
    repository = PharmaciesRepository()
    use_case = PharmacieFinder(repository)
    controller = PharmacieFinderController(use_case)

    return controller.handle
