{% set include_guard = filename.replace('.', '_').upper() %}
#ifndef {{ include_guard }}
#define {{ include_guard }}

#include <QObject>

class {{ class_name }} : public QObject {
    Q_OBJECT
{% for property in properties %}
    Q_PROPERTY({{ property.type }} {{ property.name }} READ {{ property.name }} WRITE {{ property.setter_name }} NOTIFY {{ property.name}}Changed)
{% endfor %}
public:
    explicit {{ class_name }}(QObject* parent = nullptr);

{% for property in properties %}
    {{ property.type }} {{ property.name }}() const;
    void {{property.setter_name }}({{ property.arg_type }} value);
{% endfor %}

signals:
{% for property in properties %}
    void {{property.name }}Changed({{ property.arg_type }} value);
{% endfor %}

protected:
{% for property in properties %}
    {{ property.type }} {{ property.var_name }}{% if property.value is defined %} = {{ property.value }}{% endif %};
{% endfor %}
};

#endif // {{ include_guard }}

