import i18n
from i18n import t

# Required settings
i18n.set('load_path', [r'./translations'])  # set list of folders, which contain translations
i18n.set('available_locales', ['en', 'sk'])
i18n.set('locale', 'sk')  # set default locale

# Other useful settings
i18n.set('error_on_missing_translation', True)
i18n.set('error_on_missing_placeholder', True)
i18n.set('error_on_missing_plural', True)
i18n.set('plural_few', 4)
i18n.set('filename_format', '{locale}.{format}')
i18n.set('fallback', 'en')
i18n.set('enable_memoization', True)

# See all configuration options
print('\nPrint all settings:')
print('---------------------------')
print(i18n.config.settings)


print('\nTest slovak locale:')
print('---------------------------')
i18n.set('locale', 'sk')
print(t('hi'))
print(t('mail_number', count=0))
print(t('mail_number', count=1))
print(t('mail_number', count=4))
print(t('mail_number', count=10))


print('\nTest english locale:')
print('---------------------------')
i18n.set('locale', 'en')
print(t('hi'))
print(t('mail_number', count=0))
print(t('mail_number', count=1))
print(t('mail_number', count=4))
print(t('mail_number', count=10))

print('\nTest switching locale:')
print('---------------------------')
print(t('hi', locale='sk'))
print(t('hi', locale='en'))
print(t('free_sentence', locale='sk'))
