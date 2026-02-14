#!/usr/bin/env python3
"""
Script para identificar a stack tecnológica do projeto.

Escaneia arquivos de configuração de diversas linguagens/frameworks,
extrai tecnologias com suas versões, e mapeia para IDs de documentação
do Context7 para consulta.
"""

import os
import sys
import json
import re


# ─── Mapeamento de tecnologias para Context7 library IDs e doc URLs ────────

CONTEXT7_DOCS = {
    # JavaScript / TypeScript
    "react": {"context7": "/facebook/react", "docs": "https://react.dev"},
    "next": {"context7": "/vercel/next.js", "docs": "https://nextjs.org/docs"},
    "vue": {"context7": "/vuejs/vue", "docs": "https://vuejs.org/guide"},
    "nuxt": {"context7": "/nuxt/nuxt", "docs": "https://nuxt.com/docs"},
    "angular": {"context7": "/angular/angular", "docs": "https://angular.dev/overview"},
    "svelte": {"context7": "/sveltejs/svelte", "docs": "https://svelte.dev/docs"},
    "express": {"context7": "/expressjs/express", "docs": "https://expressjs.com"},
    "nestjs": {"context7": "/nestjs/nest", "docs": "https://docs.nestjs.com"},
    "typescript": {"context7": "/microsoft/typescript", "docs": "https://www.typescriptlang.org/docs"},
    "tailwindcss": {"context7": "/tailwindlabs/tailwindcss", "docs": "https://tailwindcss.com/docs"},
    "prisma": {"context7": "/prisma/prisma", "docs": "https://www.prisma.io/docs"},
    "drizzle-orm": {"context7": "/drizzle-team/drizzle-orm", "docs": "https://orm.drizzle.team/docs/overview"},
    "vite": {"context7": "/vitejs/vite", "docs": "https://vite.dev/guide"},
    "vitest": {"context7": "/vitest-dev/vitest", "docs": "https://vitest.dev/guide"},
    "jest": {"context7": "/jestjs/jest", "docs": "https://jestjs.io/docs/getting-started"},
    "cypress": {"context7": "/cypress-io/cypress", "docs": "https://docs.cypress.io"},
    "playwright": {"context7": "/microsoft/playwright", "docs": "https://playwright.dev/docs/intro"},
    "zustand": {"context7": "/pmndrs/zustand", "docs": "https://zustand-demo.pmnd.rs"},
    "redux": {"context7": "/reduxjs/redux", "docs": "https://redux.js.org"},
    "axios": {"context7": "/axios/axios", "docs": "https://axios-http.com/docs/intro"},
    "shadcn-ui": {"context7": "/shadcn-ui/ui", "docs": "https://ui.shadcn.com/docs"},
    "radix-ui": {"context7": "/radix-ui/primitives", "docs": "https://www.radix-ui.com/docs/primitives"},
    "storybook": {"context7": "/storybookjs/storybook", "docs": "https://storybook.js.org/docs"},
    "astro": {"context7": "/withastro/astro", "docs": "https://docs.astro.build"},
    "remix": {"context7": "/remix-run/remix", "docs": "https://remix.run/docs"},
    "bun": {"context7": "/oven-sh/bun", "docs": "https://bun.sh/docs"},
    "deno": {"context7": "/denoland/deno", "docs": "https://docs.deno.com"},
    "node": {"context7": "/nodejs/node", "docs": "https://nodejs.org/docs"},
    "pnpm": {"context7": "/pnpm/pnpm", "docs": "https://pnpm.io"},
    "eslint": {"context7": "/eslint/eslint", "docs": "https://eslint.org/docs/latest"},

    # PHP
    "laravel": {"context7": "/laravel/framework", "docs": "https://laravel.com/docs"},
    "symfony": {"context7": "/symfony/symfony", "docs": "https://symfony.com/doc/current"},
    "livewire": {"context7": "/livewire/livewire", "docs": "https://livewire.laravel.com/docs"},
    "filament": {"context7": "/filamentphp/filament", "docs": "https://filamentphp.com/docs"},
    "inertiajs": {"context7": "/inertiajs/inertia", "docs": "https://inertiajs.com"},
    "phpunit": {"context7": "/sebastianbergmann/phpunit", "docs": "https://docs.phpunit.de"},
    "pest": {"context7": "/pestphp/pest", "docs": "https://pestphp.com/docs"},

    # Python
    "django": {"context7": "/django/django", "docs": "https://docs.djangoproject.com"},
    "flask": {"context7": "/pallets/flask", "docs": "https://flask.palletsprojects.com"},
    "fastapi": {"context7": "/tiangolo/fastapi", "docs": "https://fastapi.tiangolo.com"},
    "sqlalchemy": {"context7": "/sqlalchemy/sqlalchemy", "docs": "https://docs.sqlalchemy.org"},
    "pydantic": {"context7": "/pydantic/pydantic", "docs": "https://docs.pydantic.dev"},
    "pytest": {"context7": "/pytest-dev/pytest", "docs": "https://docs.pytest.org"},
    "celery": {"context7": "/celery/celery", "docs": "https://docs.celeryq.dev"},
    "poetry": {"context7": "/python-poetry/poetry", "docs": "https://python-poetry.org/docs"},

    # Ruby
    "rails": {"context7": "/rails/rails", "docs": "https://guides.rubyonrails.org"},
    "rspec": {"context7": "/rspec/rspec", "docs": "https://rspec.info/documentation"},

    # Go
    "gin": {"context7": "/gin-gonic/gin", "docs": "https://gin-gonic.com/docs"},
    "echo": {"context7": "/labstack/echo", "docs": "https://echo.labstack.com/docs"},
    "fiber": {"context7": "/gofiber/fiber", "docs": "https://docs.gofiber.io"},

    # Rust
    "actix-web": {"context7": "/actix/actix-web", "docs": "https://actix.rs/docs"},
    "tokio": {"context7": "/tokio-rs/tokio", "docs": "https://tokio.rs"},
    "axum": {"context7": "/tokio-rs/axum", "docs": "https://docs.rs/axum/latest/axum"},

    # Databases
    "postgresql": {"context7": "/postgres/postgres", "docs": "https://www.postgresql.org/docs"},
    "mysql": {"context7": "/mysql/mysql-server", "docs": "https://dev.mysql.com/doc"},
    "mongodb": {"context7": "/mongodb/docs", "docs": "https://www.mongodb.com/docs"},
    "redis": {"context7": "/redis/redis", "docs": "https://redis.io/docs"},
    "sqlite": {"context7": "/sqlite/sqlite", "docs": "https://www.sqlite.org/docs.html"},
    "supabase": {"context7": "/supabase/supabase", "docs": "https://supabase.com/docs"},
    "firebase": {"context7": "/firebase/firebase-js-sdk", "docs": "https://firebase.google.com/docs"},

    # Infrastructure / DevOps
    "docker": {"context7": "/docker/docs", "docs": "https://docs.docker.com"},
    "terraform": {"context7": "/hashicorp/terraform", "docs": "https://developer.hashicorp.com/terraform/docs"},
    "kubernetes": {"context7": "/kubernetes/kubernetes", "docs": "https://kubernetes.io/docs"},

    # Mobile
    "react-native": {"context7": "/facebook/react-native", "docs": "https://reactnative.dev/docs/getting-started"},
    "flutter": {"context7": "/flutter/flutter", "docs": "https://docs.flutter.dev"},
    "expo": {"context7": "/expo/expo", "docs": "https://docs.expo.dev"},
}


def find_config_files(project_root: str) -> dict:
    """Encontra arquivos de configuração relevantes no projeto."""
    config_patterns = {
        "package.json": "npm/node",
        "package-lock.json": "npm",
        "yarn.lock": "yarn",
        "pnpm-lock.yaml": "pnpm",
        "bun.lockb": "bun",
        "composer.json": "php/composer",
        "composer.lock": "php/composer",
        "requirements.txt": "python/pip",
        "pyproject.toml": "python/pyproject",
        "setup.py": "python/setuptools",
        "Pipfile": "python/pipenv",
        "poetry.lock": "python/poetry",
        "Gemfile": "ruby/bundler",
        "Gemfile.lock": "ruby/bundler",
        "go.mod": "go",
        "go.sum": "go",
        "Cargo.toml": "rust/cargo",
        "Cargo.lock": "rust/cargo",
        "docker-compose.yml": "docker",
        "docker-compose.yaml": "docker",
        "Dockerfile": "docker",
        ".env.example": "env",
        ".env": "env",
        "tsconfig.json": "typescript",
        "tailwind.config.js": "tailwindcss",
        "tailwind.config.ts": "tailwindcss",
        "tailwind.config.mjs": "tailwindcss",
        "vite.config.js": "vite",
        "vite.config.ts": "vite",
        "next.config.js": "nextjs",
        "next.config.mjs": "nextjs",
        "next.config.ts": "nextjs",
        "nuxt.config.ts": "nuxt",
        "nuxt.config.js": "nuxt",
        "astro.config.mjs": "astro",
        "svelte.config.js": "svelte",
        "angular.json": "angular",
        ".eslintrc.js": "eslint",
        ".eslintrc.json": "eslint",
        "eslint.config.js": "eslint",
        "jest.config.js": "jest",
        "jest.config.ts": "jest",
        "vitest.config.ts": "vitest",
        "vitest.config.js": "vitest",
        "cypress.config.js": "cypress",
        "cypress.config.ts": "cypress",
        "playwright.config.ts": "playwright",
        "phpunit.xml": "phpunit",
        "phpunit.xml.dist": "phpunit",
        "artisan": "laravel",
    }

    found = {}
    for filename, tech_hint in config_patterns.items():
        filepath = os.path.join(project_root, filename)
        if os.path.isfile(filepath):
            found[filename] = {
                "path": filepath,
                "tech_hint": tech_hint,
            }

    return found


def parse_package_json(filepath: str) -> dict:
    """Extrai tecnologias e versões do package.json."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, OSError):
        return {}

    result = {
        "name": data.get("name", ""),
        "engines": data.get("engines", {}),
        "dependencies": {},
        "devDependencies": {},
    }

    for dep, version in data.get("dependencies", {}).items():
        result["dependencies"][dep] = version

    for dep, version in data.get("devDependencies", {}).items():
        result["devDependencies"][dep] = version

    return result


def parse_composer_json(filepath: str) -> dict:
    """Extrai tecnologias e versões do composer.json."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, OSError):
        return {}

    result = {
        "name": data.get("name", ""),
        "require": data.get("require", {}),
        "require-dev": data.get("require-dev", {}),
    }

    return result


def parse_requirements_txt(filepath: str) -> dict:
    """Extrai pacotes e versões do requirements.txt."""
    result = {}
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or line.startswith("-"):
                    continue
                match = re.match(r"^([a-zA-Z0-9_.-]+)\s*([><=!~]+\s*[\d.]+)?", line)
                if match:
                    pkg = match.group(1)
                    ver = match.group(2).strip() if match.group(2) else "*"
                    result[pkg] = ver
    except OSError:
        pass
    return result


def parse_pyproject_toml(filepath: str) -> dict:
    """Extrai informações básicas do pyproject.toml."""
    result = {"dependencies": {}, "python_version": ""}
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # Python version
        py_match = re.search(r'python\s*=\s*"([^"]+)"', content)
        if py_match:
            result["python_version"] = py_match.group(1)

        # Dependencies (basic parsing)
        dep_matches = re.findall(r'^([a-zA-Z0-9_-]+)\s*=\s*["\{]([^"\}]+)', content, re.MULTILINE)
        for pkg, ver in dep_matches:
            if pkg not in ("name", "version", "description", "authors", "readme", "python"):
                result["dependencies"][pkg] = ver

    except OSError:
        pass
    return result


def parse_go_mod(filepath: str) -> dict:
    """Extrai módulos e versões do go.mod."""
    result = {"go_version": "", "modules": {}}
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        go_match = re.search(r"^go\s+([\d.]+)", content, re.MULTILINE)
        if go_match:
            result["go_version"] = go_match.group(1)

        require_matches = re.findall(r"^\s+(\S+)\s+(v[\d.]+\S*)", content, re.MULTILINE)
        for mod, ver in require_matches:
            result["modules"][mod] = ver

    except OSError:
        pass
    return result


def parse_cargo_toml(filepath: str) -> dict:
    """Extrai crates e versões do Cargo.toml."""
    result = {"rust_edition": "", "dependencies": {}}
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        edition_match = re.search(r'edition\s*=\s*"(\d+)"', content)
        if edition_match:
            result["rust_edition"] = edition_match.group(1)

        dep_matches = re.findall(r'^([a-zA-Z0-9_-]+)\s*=\s*"([^"]+)"', content, re.MULTILINE)
        for crate, ver in dep_matches:
            if crate not in ("name", "version", "edition", "description"):
                result["dependencies"][crate] = ver

    except OSError:
        pass
    return result


def parse_gemfile(filepath: str) -> dict:
    """Extrai gems e versões do Gemfile."""
    result = {"ruby_version": "", "gems": {}}
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        ruby_match = re.search(r"ruby\s+['\"]([^'\"]+)", content)
        if ruby_match:
            result["ruby_version"] = ruby_match.group(1)

        gem_matches = re.findall(r"gem\s+['\"]([^'\"]+)['\"](?:\s*,\s*['\"]([^'\"]*)['\"])?", content)
        for gem, ver in gem_matches:
            result["gems"][gem] = ver if ver else "*"

    except OSError:
        pass
    return result


def parse_docker_compose(filepath: str) -> dict:
    """Extrai serviços e imagens do docker-compose."""
    result = {"services": {}}
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # Basic parsing for image lines
        service_blocks = re.findall(
            r"^\s{2}(\w[\w-]*):\s*\n((?:\s{4,}.+\n)*)",
            content,
            re.MULTILINE,
        )
        for svc_name, svc_body in service_blocks:
            image_match = re.search(r"image:\s*(\S+)", svc_body)
            if image_match:
                result["services"][svc_name] = image_match.group(1)
            else:
                result["services"][svc_name] = "build (Dockerfile)"

    except OSError:
        pass
    return result


def match_documentation(technologies: list[str]) -> list[dict]:
    """Mapeia tecnologias detectadas para documentação Context7."""
    docs = []
    seen = set()

    for tech in technologies:
        tech_lower = tech.lower().strip()

        # Normalizar nomes comuns
        aliases = {
            "next.js": "next", "nextjs": "next",
            "vue.js": "vue", "vuejs": "vue",
            "nuxt.js": "nuxt", "nuxtjs": "nuxt",
            "react-dom": "react",
            "tailwind": "tailwindcss",
            "@tailwindcss/": "tailwindcss",
            "laravel/framework": "laravel",
            "laravel/sail": "laravel",
            "laravel/sanctum": "laravel",
            "laravel/breeze": "laravel",
            "laravel/jetstream": "laravel",
            "react-native": "react-native",
            "@nestjs/": "nestjs",
            "@prisma/client": "prisma",
            "drizzle-orm": "drizzle-orm",
            "pg": "postgresql",
            "mysql2": "mysql",
            "better-sqlite3": "sqlite",
            "@supabase/supabase-js": "supabase",
            "firebase": "firebase",
            "ioredis": "redis",
        }

        resolved = tech_lower
        for alias, target in aliases.items():
            if tech_lower == alias or tech_lower.startswith(alias):
                resolved = target
                break

        if resolved in CONTEXT7_DOCS and resolved not in seen:
            seen.add(resolved)
            info = CONTEXT7_DOCS[resolved]
            docs.append({
                "technology": resolved,
                "detected_as": tech,
                "context7_id": info["context7"],
                "documentation_url": info["docs"],
            })

    return docs


def identify_stack(project_root: str) -> dict:
    """Função principal que identifica toda a stack do projeto."""
    config_files = find_config_files(project_root)

    stack = {
        "project_root": project_root,
        "config_files_found": list(config_files.keys()),
        "languages": [],
        "frameworks": [],
        "databases": [],
        "infrastructure": [],
        "testing": [],
        "all_dependencies": {},
        "documentation_links": [],
    }

    all_techs = set()

    # ─── Node.js / JavaScript / TypeScript ───
    if "package.json" in config_files:
        pkg = parse_package_json(config_files["package.json"]["path"])
        all_deps = {**pkg.get("dependencies", {}), **pkg.get("devDependencies", {})}
        stack["all_dependencies"]["npm"] = all_deps

        if pkg.get("engines", {}).get("node"):
            stack["languages"].append({"name": "Node.js", "version": pkg["engines"]["node"]})
            all_techs.add("node")

        for dep_name in all_deps:
            all_techs.add(dep_name)

    if "tsconfig.json" in config_files:
        stack["languages"].append({"name": "TypeScript", "version": "see tsconfig.json"})
        all_techs.add("typescript")

    # ─── PHP / Composer ───
    if "composer.json" in config_files:
        composer = parse_composer_json(config_files["composer.json"]["path"])
        all_deps = {**composer.get("require", {}), **composer.get("require-dev", {})}
        stack["all_dependencies"]["composer"] = all_deps

        if "php" in all_deps:
            stack["languages"].append({"name": "PHP", "version": all_deps["php"]})

        for dep_name in all_deps:
            all_techs.add(dep_name)

    if "artisan" in config_files:
        all_techs.add("laravel")

    # ─── Python ───
    if "requirements.txt" in config_files:
        reqs = parse_requirements_txt(config_files["requirements.txt"]["path"])
        stack["all_dependencies"]["pip"] = reqs
        stack["languages"].append({"name": "Python", "version": "see requirements.txt"})
        for pkg_name in reqs:
            all_techs.add(pkg_name)

    if "pyproject.toml" in config_files:
        pyproj = parse_pyproject_toml(config_files["pyproject.toml"]["path"])
        stack["all_dependencies"]["pyproject"] = pyproj.get("dependencies", {})
        if pyproj.get("python_version"):
            stack["languages"].append({"name": "Python", "version": pyproj["python_version"]})
        for pkg_name in pyproj.get("dependencies", {}):
            all_techs.add(pkg_name)

    # ─── Go ───
    if "go.mod" in config_files:
        gomod = parse_go_mod(config_files["go.mod"]["path"])
        stack["all_dependencies"]["go"] = gomod.get("modules", {})
        if gomod.get("go_version"):
            stack["languages"].append({"name": "Go", "version": gomod["go_version"]})
        for mod_name in gomod.get("modules", {}):
            all_techs.add(mod_name.split("/")[-1])

    # ─── Rust ───
    if "Cargo.toml" in config_files:
        cargo = parse_cargo_toml(config_files["Cargo.toml"]["path"])
        stack["all_dependencies"]["cargo"] = cargo.get("dependencies", {})
        if cargo.get("rust_edition"):
            stack["languages"].append({"name": "Rust", "version": f"edition {cargo['rust_edition']}"})
        for crate_name in cargo.get("dependencies", {}):
            all_techs.add(crate_name)

    # ─── Ruby ───
    if "Gemfile" in config_files:
        gemfile = parse_gemfile(config_files["Gemfile"]["path"])
        stack["all_dependencies"]["bundler"] = gemfile.get("gems", {})
        if gemfile.get("ruby_version"):
            stack["languages"].append({"name": "Ruby", "version": gemfile["ruby_version"]})
        for gem_name in gemfile.get("gems", {}):
            all_techs.add(gem_name)

    # ─── Docker / Infrastructure ───
    docker_compose_file = None
    if "docker-compose.yml" in config_files:
        docker_compose_file = config_files["docker-compose.yml"]["path"]
    elif "docker-compose.yaml" in config_files:
        docker_compose_file = config_files["docker-compose.yaml"]["path"]

    if docker_compose_file:
        dc = parse_docker_compose(docker_compose_file)
        stack["infrastructure"].append({"name": "Docker Compose", "services": dc.get("services", {})})
        all_techs.add("docker")

        # Detectar databases nas imagens
        for svc, image in dc.get("services", {}).items():
            img_lower = image.lower()
            if "postgres" in img_lower:
                version = re.search(r":(\d[\d.]*)", image)
                stack["databases"].append({"name": "PostgreSQL", "version": version.group(1) if version else "*"})
                all_techs.add("postgresql")
            elif "mysql" in img_lower or "mariadb" in img_lower:
                version = re.search(r":(\d[\d.]*)", image)
                stack["databases"].append({"name": "MySQL/MariaDB", "version": version.group(1) if version else "*"})
                all_techs.add("mysql")
            elif "mongo" in img_lower:
                version = re.search(r":(\d[\d.]*)", image)
                stack["databases"].append({"name": "MongoDB", "version": version.group(1) if version else "*"})
                all_techs.add("mongodb")
            elif "redis" in img_lower:
                version = re.search(r":(\d[\d.]*)", image)
                stack["databases"].append({"name": "Redis", "version": version.group(1) if version else "*"})
                all_techs.add("redis")

    if "Dockerfile" in config_files:
        all_techs.add("docker")

    # ─── Package manager detection ───
    if "pnpm-lock.yaml" in config_files:
        stack["infrastructure"].append({"name": "pnpm", "version": "see lockfile"})
        all_techs.add("pnpm")
    elif "yarn.lock" in config_files:
        stack["infrastructure"].append({"name": "Yarn", "version": "see lockfile"})
    elif "bun.lockb" in config_files:
        stack["infrastructure"].append({"name": "Bun", "version": "see lockfile"})
        all_techs.add("bun")

    if "poetry.lock" in config_files:
        all_techs.add("poetry")

    # ─── Match documentation ───
    stack["documentation_links"] = match_documentation(list(all_techs))

    return stack


def main():
    """Entry point principal."""
    project_root = os.environ.get("PROJECT_ROOT", "")

    if len(sys.argv) > 1:
        project_root = sys.argv[1]

    if not project_root:
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    if not os.path.isdir(project_root):
        print(json.dumps({"error": f"Diretório não encontrado: {project_root}"}), file=sys.stderr)
        sys.exit(1)

    result = identify_stack(project_root)
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
