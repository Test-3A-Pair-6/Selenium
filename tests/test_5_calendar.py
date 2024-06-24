from datetime import date, timedelta

from pages import page_5_calendar
from utils import Driver, ConfigReader as cr, Constants as const


class TestCalendar:
    def setup_method(self):
        self.driver = Driver.get_driver()
        self.driver.get(cr.read_config("url_main"))
        self.page = page_5_calendar.PageCalendar(self.driver)

    def teardown_method(self):
        self.driver.quit()

    def prc_calendar(self):
        self.page.main_page()
        self.page.button_calendar.click()
        self.page.calendar_page()
        self.page.button_ended.click()
        self.page.button_continue.click()
        self.page.button_bought.click()
        self.page.button_not_started.click()

    def test_calendar_view(self):
        self.prc_calendar()
        self.page.buttons_clicked()
        assert len(self.page.lesson_list) > 0, "There is no lesson in the calendar"
        Driver.screenshot(self.driver, "../screenshots/screenshots_5_calendar", "calendar.png")
        self.page.button_close.click()
        assert self.page.logo.is_displayed(), "Calendar is not closed"
        Driver.screenshot(self.driver, "../screenshots/screenshots_5_calendar", "calendar_closed.png", 0.5)

    def test_calendar_lesson_find(self):
        self.prc_calendar()
        self.page.button_lesson_search.send_keys(const.lesson_name)
        self.page.searched()
        lesson_found = False
        for lesson in self.page.searched_lesson_list:
            if const.lesson_name in lesson.text:
                lesson_found = True
                break
        assert lesson_found, "Lesson not found"
        Driver.screenshot(self.driver, "../screenshots/screenshots_5_calendar", "lesson_searched.png")

    def test_calendar_instructor_find(self):
        self.prc_calendar()
        self.page.button_instructor_search.send_keys(const.instructor_name)
        self.page.searched()
        instructor_found = False
        for lesson in self.page.searched_lesson_list:
            if const.instructor_name in lesson.text:
                instructor_found = True
                break
        assert instructor_found, "Instructor not found"
        Driver.screenshot(self.driver, "../screenshots/screenshots_5_calendar", "instructor_searched.png")

    def test_calendar_lesson_instructor_find(self):
        self.prc_calendar()
        self.page.button_lesson_search.send_keys(const.lesson_name)
        self.page.button_instructor_search.send_keys(const.instructor_name)
        self.page.searched()
        founded = [False, False]
        for lesson in self.page.searched_lesson_list:
            if not founded[0] and const.lesson_name in lesson.text:
                founded[0] = True
            if not founded[1] and const.instructor_name in lesson.text:
                founded[1] = True
        assert founded[0] and founded[1], f"Lesson or instructor not found. lesson={founded[0]}instructor={founded[1]}"
        Driver.screenshot(self.driver, "../screenshots/screenshots_5_calendar", "together_searched.png")

    def test_calendar_date_orientation(self):
        self.page.main_page()
        self.page.button_calendar.click()
        self.page.date_orientation()
        month = const.months[(const.months.index(self.page.toolbar_title.text.split()[0]))]
        year = const.year + 1 if month == 'Aralık' else const.year
        self.page.date_forward.click()
        forward_month = const.months[(const.months.index(self.page.toolbar_title.text.split()[0]))]
        self.page.toolbar()
        assert self.page.toolbar_title.text == f"{forward_month} {year}", "forward date is wrong"
        Driver.screenshot(self.driver, "../screenshots/screenshots_5_calendar", "forward_month.png")
        self.page.button_day.click()
        self.page.toolbar()
        assert self.page.toolbar_title.text == f"1 {forward_month} {year}", "day view is wrong"
        Driver.screenshot(self.driver, "../screenshots/screenshots_5_calendar", "day_view.png")
        self.page.button_week.click()
        self.page.toolbar()
        day = date(const.year, const.months.index(forward_month) + 1, 1)
        start_of_week = day - timedelta(days=(day.weekday() + 1) - 1)
        end_of_week = start_of_week + timedelta(days=6)
        assert self.page.toolbar_title.text == f"{start_of_week.day} – {end_of_week.day} {forward_month[:3]} {year}"
        Driver.screenshot(self.driver, "../screenshots/screenshots_5_calendar", "week_view.png")
        self.page.button_month.click()
        self.page.toolbar()
        assert self.page.toolbar_title.text == f"{forward_month} {year}", "month view is wrong"
        Driver.screenshot(self.driver, "../screenshots/screenshots_5_calendar", "month_view.png")
