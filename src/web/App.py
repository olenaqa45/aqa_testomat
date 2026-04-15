from playwright.sync_api import Page

from web.pages.LoginPage import LoginPage
from web.pages.HomePage import HomePage
from web.pages.ProjectPage import ProjectPage
from web.pages.ProjectsPage import ProjectsPage
from web.pages.NewProjectsPage import NewProjectsPage


class App:
    def __init__(self, page: Page):
        self.page = page
        self.login_page = LoginPage(page)
        self.home_page = HomePage(page)
        self.project_page = ProjectPage(page)
        self.projects_page = ProjectsPage(page)
        self.new_projects_page = NewProjectsPage(page)
