class CodeforcesConfigs:
    user = 'williamkenzot'
    cf_url = 'http://codeforces.com/submissions/' + user

    pagination_class_name = 'pagination'
    page_numbers_xpath = '//ul/li/span/a'

    table_row_xpath = '//table/tbody/tr'

    def get_page(self, num: int):
        return self.cf_url + '/page/' + str(num)


class GithubConfigs:
    user = 'williamtsutumi'
    gh_url = 'https://github.com/' + user

    no_contribution_text = 'No contributions on '
    first_tooltip = 7
