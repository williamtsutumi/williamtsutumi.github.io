class CodeforcesConfigs:
    user = 'williamkenzot'
    cf_url = 'http://codeforces.com/submissions/' + user

    pagination_class_name = 'pagination'
    page_numbers_xpath = '//ul/li/span/a'

    table_row_xpath = '//table/tbody/tr'

    def get_page(self, num: int):
        return self.cf_url + '/page/' + str(num)


class GithubConfigs:
    first_year = 2021
    user = 'williamtsutumi'
    gh_url = 'https://github.com/' + user

    def contr_url(self, year: str):
        return 'https://github.com/williamtsutumi?tab=overview&from=' + year + '-01-01&to=' + year + '-12-31'

    no_contribution_text = 'No contributions on '
    first_tooltip = 7
