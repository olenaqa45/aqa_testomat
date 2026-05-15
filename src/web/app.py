from playwright.sync_api import Page

from web.components.header_nav import HeaderNav
from web.components.profile_menu import ProfileMenu
from web.pages.home_page import HomePage
from web.pages.login_page import LoginPage
from web.pages.new_projects_page import NewProjectsPage
from web.pages.project_page import ProjectPage
from web.pages.projects_page import ProjectsPage


class App:
    def __init__(self, page: Page):
        self.page = page
        self.login_page = LoginPage(page)
        self.home_page = HomePage(page)
        self.project_page = ProjectPage(page)
        self.projects_page = ProjectsPage(page)
        self.new_projects_page = NewProjectsPage(page)
        self.profile_menu = ProfileMenu(page)
        self.header_nav = HeaderNav(page)
