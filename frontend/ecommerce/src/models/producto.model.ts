export class Producto {
    id: number;
    codigo: string;
    nombre: string;
    descripcion: string;
    costo: number;
    precio: number;
    stock: number;
    ubicacion: string;
    categoria_fk: number | null;
    proveedor_fk: number | null;
    negocio_fk: number;
    categoria_nombre: string;
    proveedor_nombre: string;
    negocio_nombre: string;
}